Name:		texlive-puyotikz
Version:	57254
Release:	2
Summary:	Quickly typeset board states of Puyo Puyo games
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/puyotikz
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/puyotikz.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/puyotikz.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package permits to quickly typeset board states of
Puyo Puyo games. It supports large and small boards with
arbitrary shape, hidden rows, current and next puyos, labels
and move planning markers. The package requires Python3 in
support of scripts driven by PythonTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/puyotikz
%{_texmfdistdir}/scripts/puyotikz
%doc %{_texmfdistdir}/doc/latex/puyotikz

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
