Name: containerd
Version: %{?version}%{!?version:1}
Release: %{?release}%{!?release:1}%{?dist}
Summary: containerd (loong64)
License: Apache-2.0
URL: https://github.com/kubernetes-loong64/containerd-loong64
BugURL: https://github.com/kubernetes-loong64/containerd-loong64/issues
Packager: 徐晓伟 <xuxiaowei@xuxiaowei.com.cn>

# Disable strip and build-id links for cross-compiled loongarch64 binary
%global _build_id_links none
%define __strip /bin/true

%description
containerd container runtime binaries for the loong64 (LoongArch) architecture.

%prep
# This example has no source, so nothing here

%build
# Generate the script directly

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 ctr %{buildroot}/usr/bin/ctr
install -m 755 containerd %{buildroot}/usr/bin/containerd
install -m 755 containerd-shim-runc-v2 %{buildroot}/usr/bin/containerd-shim-runc-v2
install -m 755 containerd-stress %{buildroot}/usr/bin/containerd-stress

mkdir -p %{buildroot}/usr/share/man/man1/
install -m 644 man/ctr.1 %{buildroot}/usr/share/man/man1/ctr.1
install -m 644 man/containerd.1 %{buildroot}/usr/share/man/man1/containerd.1

mkdir -p %{buildroot}/usr/share/licenses/%{name}/
install -m 644 LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE

%files
%license /usr/share/licenses/%{name}/LICENSE
/usr/bin/ctr
/usr/bin/containerd
/usr/bin/containerd-shim-runc-v2
/usr/bin/containerd-stress
/usr/share/man/man1/ctr.1*
/usr/share/man/man1/containerd.1*

%changelog
