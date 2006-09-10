# NOTES:
#	- maybe espeak is better name for spec
#	- in the absence of data files in expected location (/usr/share/espeak-data or $HOME/espeak-data) program segfaults
#	
Summary:	eSpeak - speech synthesizer for English and other languages
Summary(pl):	eSpeak - syntezator mowy dla j�zyka angielskiego i innych
Name:		speak
Version:	1.13
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/espeak/%{name}-%{version}-source.zip
# Source0-md5:	1cd76ad278fa134eced57b865b72175b
Patch0:		%{name}-ac_am.patch
URL:		http://espeak.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	portaudio-devel >= 19
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eSpeak is a software speech synthesizer for English and other
languages. eSpeak produces good quality English speech. It uses a
different synthesis method from other open source TTS engines, and
sounds quite different. It's perhaps not as natural or "smooth", but I
find the articulation clearer and easier to listen to for long
periods.
- It can run as a command line program to speak text from a file or
  from stdin. A library version is also available (isn't available in
  this package).
- Includes different Voices, whose characteristics can be altered.
- Can produce speech output as a WAV file.
- SSML (Speech Synthesis Markup Language) is supported (not complete),
  and also HTML.
- Compact size. The program and its data, including several languages,
  totals about 420 kbytes.
- Can translate text to phoneme codes, so it could be adapted as a
  front end for another speech synthesis engine.
- Potential for other languages. Several are included (e.gj. polish
  language) in varying stages of progress. Help from native speakers
  for these or other languages is welcomed.
- Development tools available for producing and tuning phoneme data.
- Written in C++.

It works well as a "Talker" with the KDE text to speech system (KTTS),
as an alternative to Festival for example. As such, it can speak text
which has been selected into the clipboard, or directly from the
Konquerer browser or the Kate editor.

%description -l pl
eSpeak to programowy syntezator mowy dla angielskiego i innych
j�zyk�w. Odtwarza angielsk� mow� dobrej jako�ci. U�ywa innej metody
syntezy ni� inne silniki TTS o otwartych �r�d�ach i brzmi troch�
inaczej. Nie jest mo�e tak naturalny czy "g�adki", ale autor uwa�a t�
wymow� za czystsz� i �atwiejsz� w s�uchaniu na d�u�sz� met�.

- Mo�e dzia�a� jako program z linii polece� do wymawiania tekstu z
  pliku lub standardowego wej�cia; dost�pna jest tak�e wersja w
  postaci biblioteki (nie w tym pakiecie).
- Zawiera r�ne g�osy, a ich charakterystyk� mo�na zmienia�.
- Potrafi tworzy� pliki WAV z mow�.
- Obs�ugiwany (ale nie w pe�ni) jest SSML (Speech Synthesis Markup
  Language)  oraz HTML.
- Ma�y rozmiar - program i jego dane, wraz z kilkoma j�zykami,
  mieszcz� si� w oko�o 420kB.
- Potrafi t�umaczy� tekst na kody fonem�w, wi�c mo�e by� zaadaptowany
  jako frontend dla innych silnik�w syntezy mowy.
- Potencjalnie mo�e nadawa� si� dla innych j�zyk�w; kilka jest
  do��czonych (na przyk�ad j.polski) w r�nym stadium zaawansowania.
  Mile widziana jest pomoc od os�b, dla kt�rych s� to j�zyki ojczyste.
- Dost�pne s� narz�dzia programistyczne do tworzenia i dostrajania
  danych dla fonem�w.
- Napisany w C++.

Dobrze pracuje jako "m�wca" z systemem przetwarzania tekstu na mow�
KDE (KTTS), na przyk�ad, jako alternatywa dla Festivala. Jako taki,
mo�e czyta� na g�os tekst zaznaczony uprzednio do schowka lub
bezpo�rednio z przegl�darki Konqueror i edytora Kate.

%prep
%setup -q -n %{name}-%{version}-source
%patch -p1
# remove pernicious headers to avoid using them during build instead of /usr/include/portaudio.h system header
rm -f src/portaudio{18,19,}.h

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog ReadMe docs
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/e%{name}-data
%dir %{_datadir}/e%{name}-data/voices
%dir %{_datadir}/e%{name}-data/voices/en
%{_datadir}/e%{name}-data/voices/en/en-rp-f
%{_datadir}/e%{name}-data/voices/en/en-wm-f
%{_datadir}/e%{name}-data/voices/en/en-n
%{_datadir}/e%{name}-data/voices/en/en
%{_datadir}/e%{name}-data/voices/en/en1
%{_datadir}/e%{name}-data/voices/en/en2
%{_datadir}/e%{name}-data/voices/en/en3
%{_datadir}/e%{name}-data/voices/en/en4
%{_datadir}/e%{name}-data/voices/en/en6
%{_datadir}/e%{name}-data/voices/en/en7
%{_datadir}/e%{name}-data/voices/en/en8
%{_datadir}/e%{name}-data/voices/en/en-croak
%{_datadir}/e%{name}-data/voices/en/en-f
%{_datadir}/e%{name}-data/voices/en/en-rp
%{_datadir}/e%{name}-data/voices/en/en-n-f
%{_datadir}/e%{name}-data/voices/en/en-wm
%{_datadir}/e%{name}-data/voices/es
%{_datadir}/e%{name}-data/voices/it
%{_datadir}/e%{name}-data/voices/pl
%{_datadir}/e%{name}-data/voices/af
%{_datadir}/e%{name}-data/voices/default
%{_datadir}/e%{name}-data/voices/eo
%{_datadir}/e%{name}-data/voices/de
%{_datadir}/e%{name}-data/voices/el
%dir %{_datadir}/e%{name}-data/soundicons
%{_datadir}/e%{name}-data/af_dict
%{_datadir}/e%{name}-data/de_dict
%{_datadir}/e%{name}-data/en_dict
%{_datadir}/e%{name}-data/eo_dict
%{_datadir}/e%{name}-data/es_dict
%{_datadir}/e%{name}-data/it_dict
%{_datadir}/e%{name}-data/phondata
%{_datadir}/e%{name}-data/phonindex
%{_datadir}/e%{name}-data/phontab
%{_datadir}/e%{name}-data/config
%{_datadir}/e%{name}-data/pl_dict
%{_datadir}/e%{name}-data/el_dict
