import time
from datetime import datetime, timezone
from http import cookies
from typing import Iterable, Optional


class RoutingCookieJar:
    """
    Minimal cookie jar to persist node-affinity cookies between requests.
    """

    def __init__(self) -> None:
        # (domain, path, name) -> {"value": str, "expires": Optional[float]}
        self._cookies = {}

    def store(
        self, set_cookie_headers: Iterable[str], host: str, request_path: str
    ) -> None:
        if not set_cookie_headers:
            return
        # cur query params
        request_path = request_path.split("?", 1)[0] or "/"
        default_path = self._default_path(request_path)
        for header in set_cookie_headers:
            simple = cookies.SimpleCookie()
            try:
                simple.load(header)
            except (cookies.CookieError, KeyError):
                continue
            for morsel in simple.values():
                domain = self._normalize_domain(morsel["domain"], host)
                path = morsel["path"] or default_path
                expires = self._parse_expiry(morsel)
                key = (domain, path, morsel.key)
                self._cookies[key] = {"value": morsel.value, "expires": expires}

    def get_header(self, host: str, request_path: str) -> Optional[str]:
        if not self._cookies:
            return None

        now = time.time()
        request_path = request_path.split("?", 1)[0] or "/"
        pairs = []
        expired = []
        for (domain, path, name), meta in self._cookies.items():
            expires = meta["expires"]
            if expires is not None and expires <= now:
                expired.append((domain, path, name))
                continue
            if not self._domain_matches(host, domain):
                continue
            if not self._path_matches(request_path, path):
                continue
            pairs.append(f"{name}={meta['value']}")

        for key in expired:
            self._cookies.pop(key, None)

        return "; ".join(pairs) if pairs else None

    @staticmethod
    def _default_path(request_path: str) -> str:
        # https://www.rfc-editor.org/rfc/rfc6265#section-5.1.4 defines how default path
        # should be created
        request_path = request_path or "/"
        if not request_path.startswith("/"):
            return "/"
        if request_path == "/":
            return "/"
        slash_index = request_path.rfind("/")
        if slash_index <= 0:
            return "/"
        return request_path[:slash_index]

    @staticmethod
    def _normalize_domain(cookie_domain: str, host: str) -> str:
        if cookie_domain:
            return cookie_domain.lstrip(".").lower()
        return (host or "").lower()

    @staticmethod
    def _parse_expiry(morsel: cookies.Morsel) -> Optional[float]:
        max_age = morsel["max-age"]
        if max_age:
            try:
                return time.time() + int(max_age)
            except ValueError:
                return None
        expires = morsel["expires"]
        if expires:
            return RoutingCookieJar._parse_http_date(expires)

        return None

    @staticmethod
    def _parse_http_date(date_str: str) -> Optional[float]:
        date_str = (date_str or "").strip()
        if not date_str:
            return None
        formats = (
            ("%a, %d %b %Y %H:%M:%S GMT", False),  # IMF-fixdate (RFC 7231)
            ("%a, %d-%b-%Y %H:%M:%S GMT", False),  # RFC 850 but 4-digit year
            ("%a, %d-%b-%y %H:%M:%S GMT", True),  # RFC 850 two-digit year
            ("%A, %d-%b-%y %H:%M:%S GMT", True),  # RFC 850 weekday spelled out
        )
        for fmt, needs_adjust in formats:
            try:
                parsed = datetime.strptime(date_str, fmt)
            except (TypeError, ValueError):
                continue
            if needs_adjust:
                parsed = RoutingCookieJar._adjust_two_digit_year(parsed)
            parsed = parsed.replace(tzinfo=timezone.utc)
            return parsed.timestamp()
        return None

    @staticmethod
    def _adjust_two_digit_year(dt: datetime) -> datetime:
        year = dt.year
        if year < 100:
            if year < 70:
                year += 2000
            else:
                year += 1900
        return dt.replace(year=year)

    @staticmethod
    def _domain_matches(host: str, domain: str) -> bool:
        host = (host or "").lower()
        domain = domain or ""
        if not host or not domain:
            return False
        return host == domain or host.endswith(f".{domain}")

    @staticmethod
    def _path_matches(request_path: str, cookie_path: str) -> bool:
        request_path = request_path or "/"
        if not request_path.startswith("/"):
            request_path = "/" + request_path
        normalized = (cookie_path or "/").rstrip("/") or "/"
        if normalized == "/":
            return True
        if not request_path.startswith(normalized):
            return False
        if len(request_path) == len(normalized):
            return True
        return request_path[len(normalized)] == "/"
