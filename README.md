[![Build Status](https://img.shields.io/github/workflow/status/SSHcom/privx-sdk-for-python/Python%20package)](https://github.com/SSHcom/privx-sdk-for-python/actions)

# PrivX SDK for Python 3

The **PrivX Software Development Kit (SDK)** facilitates you with an automation of lean access management for privileged users. It offers a high-level abstraction to programmatically configure your IAM policies.

## Inspiration

Just-in-time access management is the challenging, find out more pain points from this [video](https://www.youtube.com/watch?v=Atps1AiATVs).

PrivX improves the process of granting and revoking access, ensures your admins and engineers always have one-click access to the right infrastructure resources, and gives you an audit trail - vital if you are handling sensitive data or working in IT outsourcing.

PrivX is an ultimate replacement for jump hosts and bastions. It adds traceability to shared accounts using shared passwords, and conveniently combines access management for your On-Prem, AWS, Azure and GCP infrastructure, all in one multi-cloud solution.

Learn more about [PrivX](https://www.ssh.com/products/privx) or try [Live Demo](https://info.ssh.com/privx_contact_enterprise_sales).

## Key features

This projects implements a high level Python abstraction to PrivX [REST API](https://privx.docs.ssh.com/reference).

* OAuth2 Client Authentication
* Hosts Management
* Roles Management
* Users Management

## Getting Started

The latest version of SDK is available at its `master` branch. All development, including new features and bug fixes, take place on the `master` branch using forking and pull requests as described in contribution guidelines.

The library is available using pip

```
pip install git+https://github.com/SSHcom/privx-sdk-for-python.git
```

Essentially, the library requires up-and-running PrivX instance.

Please see [examples](examples)

## How To Contribute

The SDK is [Apache 2.0](LICENSE) licensed and accepts contributions via GitHub pull requests:

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Added some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

The development requires Python 3.6 and essential build tools.

<!-- 
TODO: How to build and test library before the pull request

```bash
git clone https://github.com/SSHcom/privx-sdk-for-python
cd privx-sdk-for-python
make
make test
```
-->

### commit message

The commit message helps us to write a good release note, speed-up review process. The message should address two question what changed and why. The project follows the template defined by chapter [Contributing to a Project](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project) of Git book.

### bugs

If you experience any issues with the library, please let us know via [GitHub issues](https://github.com/SSHcom/privx-sdk-for-python/issues). We appreciate detailed and accurate reports that help us to identity and replicate the issue.

* **Specify** the configuration of your environment. Include which operating system you use and the versions of runtime environments.

* **Attach** logs, screenshots and exceptions, in possible.

* **Reveal** the steps you took to reproduce the problem, include code snippet or links to your project.

### Style

[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Documentation Status](https://readthedocs.org/projects/flake8/badge/?version=latest)](https://flake8.pycqa.org/en/latest/?badge=latest)

* Line-width is 88 symbols
* Use Type Annotation
* Use double quotes
* Use isort for sorting the imports order

``isort path --settings linter_config.cfg``

* Format code using black

``black path``

* Check PEP using flake8
``flake8 path --config ./linter_config.cfg``
  
OR use bash script
``./run_linters.sh path``

## License

[![See LICENSE](https://img.shields.io/github/license/SSHcom/privx-sdk-for-python.svg?style=for-the-badge)](LICENSE)
