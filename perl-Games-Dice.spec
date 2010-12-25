%define upstream_name    Games-Dice
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Simulates rolling dice
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Games/%{upstream_name}-%{upstream_version}.tar.gz


BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Games::Dice simulates die rolls. It uses a function-oriented (not
object-oriented) interface. No functions are exported by default. At
present, there are two functions which are exportable: 'roll' and
'roll_array'. The latter is used internally by 'roll', but can also be
exported by itself.

The number and type of dice to roll is given in a style which should be
familiar to players of popular role-playing games: _a_d_b_[+-*/b]_c_. _a_
is optional and defaults to 1; it gives the number of dice to roll. _b_
indicates the number of sides to each die; the most common, cube-shaped die
is thus a d6. % can be used instead of 100 for _b_; hence, rolling 2d% and
2d100 is equivalent. 'roll' simulates _a_ rolls of _b_-sided dice and adds
together the results. The optional end, consisting of one of +-*/b and a
number _c_, can modify the sum of the individual dice. +-*/ are similar in
that they take the sum of the rolls and add or subtract _c_, or multiply or
divide the sum by _c_. (x can also be used instead of *.) Hence, 1d6+2
gives a number in the range 3..8, and 2d4*10 gives a number in the range
20..80. (Using / truncates the result to an int after dividing.) Using b in
this slot is a little different: it's short for "best" and indicates "roll
a number of dice, but add together only the best few". For example, 5d6b3
rolls five six- sided dice and adds together the three best rolls. This is
sometimes used, for example, in roll-playing to give higher averages.

Generally, 'roll' probably provides the nicer interface, since it does the
adding up itself. However, in some situations one may wish to process the
individual rolls (for example, I am told that in the game Feng Shui, the
number of dice to be rolled cannot be determined in advance but depends on
whether any 6's were rolled); in such a case, one can use 'roll_array' to
return an array of values, which can then be examined or processed in an
application-dependent manner.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*


