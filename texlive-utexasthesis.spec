Name:		texlive-utexasthesis
Version:	48648
Release:	2
Summary:	University of Texas at Austin graduate thesis style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/utexasthesis
License:	cc0
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/utexasthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/utexasthesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class file complies with the Digital Submission
Requirement for Masters and Ph.D. thesis submissions of the
University of Texas at Austin.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/utexasthesis
%doc %{_texmfdistdir}/doc/latex/utexasthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
