# containerd for LoongArch64

<p align="center"><a href="README.md">English</a> | <a href="README-zh.md">中文</a></p>

<p align="center"><img src="https://img.shields.io/badge/containerd%20LoongArch64%20%E9%BE%99%E8%8A%AF%E6%9E%B6%E6%9E%84%E5%8F%91%E8%A1%8C%E7%89%88-blue?logo=docker&logoColor=white" alt="containerd LoongArch64 龙芯架构发行版"></p>

Build [containerd](https://github.com/containerd/containerd) binaries for the **LoongArch64 (loong64)** architecture via
CI/CD.

## How it works

A GitHub Actions workflow clones the specified containerd version, cross-compiles with
`GOOS=linux GOARCH=loong64`, and uploads the built binaries as workflow artifacts. Target platform: `linux/loong64`.

## Branch naming

Push a branch named `loong64-<containerd-version>` (e.g. `loong64-v2.3.2`) to trigger a build. Append `+<build>`
(e.g. `loong64-v2.3.2+0`) to include build metadata.

## [Release](https://github.com/kubernetes-loong64/containerd-loong64/releases)

Push a tag matching `release-loong64-<containerd-version>` (e.g. `release-loong64-v2.3.2+0`) to publish
a GitHub Release with the built binaries.

The `+<build>` suffix provides build metadata (e.g. `+0`, `+1-alpha.1`).

The suffix in the build metadata indicates the release stage:

| Suffix  | Stage         |
|---------|---------------|
| `alpha` | Internal beta |
| `beta`  | Public beta   |
| `rc`    | Pre-release   |
| (none)  | Stable        |

## Release artifacts

Each release includes the following files:

| File                      | Description                 |
|---------------------------|-----------------------------|
| `containerd`              | containerd daemon binary    |
| `containerd-shim`         | containerd shim binary      |
| `containerd-shim-runc-v1` | containerd shim for runc v1 |
| `containerd-shim-runc-v2` | containerd shim for runc v2 |
| `ctr`                     | containerd CLI tool         |

Each file has a corresponding `.asc` detached GPG signature.

## Verifying releases

- Releases are signed with GPG.
- Download the public key from [keys.openpgp.org](https://keys.openpgp.org).
- Fingerprint: [FCF8724722CCBF9F51B1FBE376532BE7E3013105](https://keys.openpgp.org/debug?q=FCF8724722CCBF9F51B1FBE376532BE7E3013105)
- [Manual download](https://keys.openpgp.org/vks/v1/by-fingerprint/FCF8724722CCBF9F51B1FBE376532BE7E3013105)

```shell
gpg --keyserver keys.openpgp.org --recv-keys FCF8724722CCBF9F51B1FBE376532BE7E3013105
echo "FCF8724722CCBF9F51B1FBE376532BE7E3013105:6:" | gpg --import-ownertrust
```

Or download the key file manually and import it:

```shell
gpg --import /tmp/xxx
```

Each release artifact has a corresponding `.asc` detached signature. To verify, download both the file and its `.asc`
signature from the release, then:

```shell
gpg --verify <file>.asc <file>
```

## Reference repositories

- [src-anolis-os/docker](https://gitee.com/src-anolis-os/docker)

## Documentation

> Applies to: moby-loong64, tini-loong64, cli-loong64, runc-loong64, containerd-loong64

- [Install containerd and docker binaries on LoongArch](https://xuxiaowei.io/t/754)
- [Install containerd and docker RPM packages on LoongArch](https://xuxiaowei.io/t/811)

## License

[Apache License 2.0](LICENSE)
