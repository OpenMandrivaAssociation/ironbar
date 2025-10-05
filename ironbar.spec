%global debug_package %{nil}

Name:       ironbar
Version:    0.17.1
Release:	1
Group:      Window Manager/Bar
URL:        https://github.com/JakeStanger/ironbar
Source0:	%{url}/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:    %{name}-%{version}-vendor.tar.gz
Summary:	Customisable Wayland gtk bar written in Rust
License:    MIT


BuildRequires: cargo
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtk-layer-shell-0)
BuildRequires: pkgconfig(libssl)
BuildRequires: lib64dbusmenu-gtk3-devel
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(luajit)
BuildRequires: lua-lgi
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libudev)

%description
%summary.

%prep
%autosetup -p1
mkdir -p .cargo

cat >> .cargo/config.toml << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

EOF

tar -xzf %{SOURCE1}

%build
cargo build --offline --release

%install
install -Dm775 target/release/ironbar %{buildroot}%{_bindir}/ironbar


%files
%{_bindir}/ironbar
