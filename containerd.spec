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

mkdir -p %{buildroot}/usr/share/licenses/%{name}/
install -m 644 LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE

mkdir -p %{buildroot}/usr/lib/systemd/system/
install -m 644 containerd.service %{buildroot}/usr/lib/systemd/system/containerd.service

%files
%license /usr/share/licenses/%{name}/LICENSE
/usr/bin/ctr
/usr/bin/containerd
/usr/bin/containerd-shim-runc-v2
/usr/bin/containerd-stress
/usr/lib/systemd/system/containerd.service

%post
if [ ! -f /etc/containerd/config.toml ]; then
    mkdir -p /etc/containerd
    containerd config default > /etc/containerd/config.toml
fi

echo "=== containerd installed ==="
echo "systemd service file: /usr/lib/systemd/system/containerd.service"
echo "Install service:"
echo "  sudo systemctl daemon-reload"
echo "  sudo systemctl enable containerd.service"
echo "  sudo systemctl start containerd.service"

%preun
echo "=== containerd uninstalling ==="
echo "Stop and remove service before uninstalling:"
echo "  sudo systemctl stop containerd.service 2>/dev/null || true"
echo "  sudo systemctl disable containerd.service 2>/dev/null || true"
echo "  sudo rm -f /etc/systemd/system/containerd.service"
echo "  sudo systemctl daemon-reload"

%changelog
