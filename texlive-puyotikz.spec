%global tl_name puyotikz
%global tl_revision 57254

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	Quickly typeset board states of Puyo Puyo games
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/puyotikz
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/puyotikz.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/puyotikz.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package permits to quickly typeset board states of Puyo Puyo
games. It supports large and small boards with arbitrary shape, hidden
rows, current and next puyos, labels and move planning markers. The
package requires Python3 in support of scripts driven by PythonTeX.

