%global tl_name vhistory
%global tl_revision 61719

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.8.0
Release:	%{tl_revision}.1
Summary:	Support for creating a change log
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/vhistory
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vhistory.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vhistory.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Vhistory simplifies the creation of a history of versions of a document.
You can easily extract information like the current version of a list of
authors from that history. It helps you to get consistent documents. The
package sets, which is used by vhistory, allows you to use sets
containing text. You can use the usual operations to create the union of
sets or the intersection of sets etc.

