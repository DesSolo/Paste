from django.conf import settings

LANGUAGE = (
    ('popular', (
        ('Python', 'Python'),
        ('Perl', 'Perl'),
        ('Ruby', 'Ruby'),
        ('PythonConsole', 'Python Console'),
        ('RubyConsole', 'Ruby Console'),
        ('PythonTraceback', 'Python Traceback'),
        ('HtmlDjango', 'Django Template'),
        ('Html', 'Html'),
        ('Text', 'Text'),
    )),
    ('ActionScript and MXML', (
        ('as3', 'ActionScript3'),
        ('as', 'ActionScript'),
        ('mxml', 'Mxml'),
        ('bc', 'BC'),
        ('gap', 'GAP'),
        ('mathematica', 'Mathematica'),
        ('mupad', 'MuPAD'),
        ('at', 'AmbientTalk'),
        ('ampl', 'Ampl'),
        ('apl', 'APL'),
        ('adl', 'Adl'),
        ('cadl', 'Cadl'),
        ('odin', 'Odin'),
        ('c-objdump', 'CObjdump'),
        ('ca65', 'Ca65'),
        ('cpp-objdump', 'CppObjdump'),
        ('d-objdump', 'DObjdump'),
        ('gas', 'Gas'),
        ('hsail', 'Hsail'),
        ('llvm', 'Llvm'),
        ('nasm', 'Nasm'),
        ('objdump-nasm', 'NasmObjdump'),
        ('objdump', 'Objdump'),
        ('tasm', 'Tasm'),
        ('autoit', 'AutoIt'),
        ('ahk', 'Autohotkey'),
        ('blitzbasic', 'BlitzBasic'),
        ('blitzmax', 'BlitzMax'),
        ('cbmbas', 'CbmBasicV2'),
        ('monkey', 'Monkey'),
        ('qbasic', 'QBasic'),
        ('bst', 'BST'),
        ('bib', 'BibTeX'),
        ('abap', 'ABAP'),
        ('cobolfree', 'CobolFreeformat'),
        ('cobol', 'Cobol'),
        ('gooddata-cl', 'GoodDataCL'),
        ('maql', 'Maql'),
        ('openedge', 'OpenEdge'),
        ('c', 'C'),
        ('cpp', 'Cpp'),
        ('arduino', 'Arduino'),
        ('clay', 'Clay'),
        ('cuda', 'Cuda'),
        ('ec', 'EC'),
        ('mql', 'Mql'),
        ('nesc', 'NesC'),
        ('pike', 'Pike'),
        ('swig', 'Swig'),
        ('vala', 'Vala'),
        ('capnp', 'CapnProto'),
        ('chapel', 'Chapel'),
        ('clean', 'Clean'),
        ('apacheconf', 'ApacheConf'),
        ('cfengine3', 'Cfengine3'),
        ('docker', 'Docker'),
        ('ini', 'Ini'),
        ('kconfig', 'Kconfig'),
        ('lighty', 'LighttpdConf'),
        ('nginx', 'NginxConf'),
        ('pacmanconf', 'PacmanConf'),
        ('pkgconfig', 'PkgConfig'),
        ('properties', 'Properties'),
        ('registry', 'Regedit'),
        ('squidconf', 'SquidConf'),
        ('termcap', 'Termcap'),
        ('terminfo', 'Terminfo'),
        ('terraform', 'Terraform'),
        ('pypylog', 'PyPyLog'),
        ('vctreestatus', 'VCTreeStatus'),
        ('cr', 'Crystal'),
        ('csound-document', 'CsoundDocument'),
        ('csound', 'CsoundOrchestra'),
        ('csound-score', 'CsoundScore'),
        ('css', 'Css'),
        ('less', 'LessCss'),
        ('sass', 'Sass'),
        ('scss', 'Scss'),
        ('croc', 'Croc'),
        ('d', 'D'),
        ('minid', 'MiniD'),
        ('smali', 'Smali'),
        ('json-object', 'JsonBareObject'),
        ('jsonld', 'JsonLd'),
        ('json', 'Json'),
        ('yaml', 'Yaml'),
        ('dpatch', 'DarcsPatch'),
        ('diff', 'Diff'),
        ('wdiff', 'WDiff'),
        ('boo', 'Boo'),
        ('aspx-cs', 'CSharpAspx'),
        ('csharp', 'CSharp'),
        ('fsharp', 'FSharp'),
        ('nemerle', 'Nemerle'),
        ('aspx-vb', 'VbNetAspx'),
        ('vb.net', 'VbNet'),
        ('alloy', 'Alloy'),
        ('bro', 'Bro'),
        ('crmsh', 'Crmsh'),
        ('flatline', 'Flatline'),
        ('mscgen', 'Mscgen'),
        ('pan', 'Pan'),
        ('protobuf', 'ProtoBuf'),
        ('puppet', 'Puppet'),
        ('rsl', 'Rsl'),
        ('snowball', 'Snowball'),
        ('thrift', 'Thrift'),
        ('vgl', 'VGL'),
        ('dylan-console', 'DylanConsole'),
        ('dylan', 'Dylan'),
        ('dylan-lid', 'DylanLid'),
        ('ecl', 'ECL'),
        ('eiffel', 'Eiffel'),
        ('elm', 'Elm'),
        ('iex', 'ElixirConsole'),
        ('elixir', 'Elixir'),
        ('erlang', 'Erlang'),
        ('erl', 'ErlangShell'),
        ('aheui', 'Aheui'),
        ('befunge', 'Befunge'),
        ('brainfuck', 'Brainfuck'),
        ('camkes', 'CAmkES'),
        ('capdl', 'CapDL'),
        ('redcode', 'Redcode'),
        ('ezhil', 'Ezhil'),
        ('factor', 'Factor'),
        ('fan', 'Fantom'),
        ('felix', 'Felix'),
        ('floscript', 'FloScript'),
        ('forth', 'Forth'),
        ('fortranfixed', 'FortranFixed'),
        ('fortran', 'Fortran'),
        ('foxpro', 'FoxPro'),
        ('go', 'Go'),
        ('abnf', 'Abnf'),
        ('bnf', 'Bnf'),
        ('jsgf', 'Jsgf'),
        ('cypher', 'Cypher'),
        ('asy', 'Asymptote'),
        ('glsl', 'GLShader'),
        ('gnuplot', 'Gnuplot'),
        ('hlsl', 'HLSLShader'),
        ('postscript', 'PostScript'),
        ('pov', 'Povray'),
        ('agda', 'Agda'),
        ('cryptol', 'Cryptol'),
        ('haskell', 'Haskell'),
        ('idris', 'Idris'),
        ('koka', 'Koka'),
        ('lagda', 'LiterateAgda'),
        ('lcry', 'LiterateCryptol'),
        ('lhs', 'LiterateHaskell'),
        ('lidr', 'LiterateIdris'),
        ('hx', 'Haxe'),
        ('haxeml', 'Hxml'),
        ('systemverilog', 'SystemVerilog'),
        ('verilog', 'Verilog'),
        ('vhdl', 'Vhdl'),
        ('hexdump', 'Hexdump'),
        ('dtd', 'Dtd'),
        ('haml', 'Haml'),
        ('html', 'Html'),
        ('pug', 'Pug'),
        ('scaml', 'Scaml'),
        ('xml', 'Xml'),
        ('xslt', 'Xslt'),
        ('idl', 'IDL'),
        ('igor', 'Igor'),
        ('limbo', 'Limbo'),
        ('control', 'DebianControl'),
        ('nsis', 'NSIS'),
        ('spec', 'RPMSpec'),
        ('sourceslist', 'SourcesList'),
        ('inform6', 'Inform6'),
        ('i6t', 'Inform6Template'),
        ('inform7', 'Inform7'),
        ('tads3', 'Tads3'),
        ('io', 'Io'),
        ('j', 'J'),
        ('coffee-script', 'CoffeeScript'),
        ('dart', 'Dart'),
        ('earl-grey', 'EarlGrey'),
        ('js', 'Javascript'),
        ('juttle', 'Juttle'),
        ('kal', 'Kal'),
        ('lasso', 'Lasso'),
        ('live-script', 'LiveScript'),
        ('mask', 'Mask'),
        ('objective-j', 'ObjectiveJ'),
        ('ts', 'TypeScript'),
        ('jlcon', 'JuliaConsole'),
        ('julia', 'Julia'),
        ('aspectj', 'AspectJ'),
        ('ceylon', 'Ceylon'),
        ('clojure', 'Clojure'),
        ('clojurescript', 'ClojureScript'),
        ('golo', 'Golo'),
        ('gosu', 'Gosu'),
        ('gst', 'GosuTemplate'),
        ('groovy', 'Groovy'),
        ('ioke', 'Ioke'),
        ('jasmin', 'Jasmin'),
        ('java', 'Java'),
        ('kotlin', 'Kotlin'),
        ('pig', 'Pig'),
        ('sarl', 'Sarl'),
        ('scala', 'Scala'),
        ('xtend', 'Xtend'),
        ('cpsa', 'CPSA'),
        ('common-lisp', 'CommonLisp'),
        ('emacs', 'EmacsLisp'),
        ('fennel', 'Fennel'),
        ('hylang', 'Hy'),
        ('newlisp', 'NewLisp'),
        ('racket', 'Racket'),
        ('scheme', 'Scheme'),
        ('shen', 'Shen'),
        ('extempore', 'Xtlang'),
        ('basemake', 'BaseMakefile'),
        ('cmake', 'CMake'),
        ('make', 'Makefile'),
        ('bbcode', 'BBCode'),
        ('groff', 'Groff'),
        ('md', 'Markdown'),
        ('trac-wiki', 'MoinWiki'),
        ('css+mozpreproc', 'MozPreprocCss'),
        ('mozhashpreproc', 'MozPreprocHash'),
        ('javascript+mozpreproc', 'MozPreprocJavascript'),
        ('mozpercentpreproc', 'MozPreprocPercent'),
        ('xul+mozpreproc', 'MozPreprocXul'),
        ('rst', 'Rst'),
        ('tex', 'Tex'),
        ('matlab', 'Matlab'),
        ('matlabsession', 'MatlabSession'),
        ('octave', 'Octave'),
        ('scilab', 'Scilab'),
        ('ocaml', 'Ocaml'),
        ('opa', 'Opa'),
        ('sml', 'SML'),
        ('bugs', 'Bugs'),
        ('jags', 'Jags'),
        ('modelica', 'Modelica'),
        ('stan', 'Stan'),
        ('modula2', 'Modula2'),
        ('monte', 'Monte'),
        ('ncl', 'NCL'),
        ('nim', 'Nimrod'),
        ('nit', 'Nit'),
        ('nixos', 'Nix'),
        ('componentpascal', 'ComponentPascal'),
        ('logos', 'Logos'),
        ('objective-c', 'ObjectiveC'),
        ('objective-c++', 'ObjectiveCpp'),
        ('swift', 'Swift'),
        ('ooc', 'Ooc'),
        ('parasail', 'ParaSail'),
        ('antlr-as', 'AntlrActionScript'),
        ('antlr-csharp', 'AntlrCSharp'),
        ('antlr-cpp', 'AntlrCpp'),
        ('antlr-java', 'AntlrJava'),
        ('antlr', 'Antlr'),
        ('antlr-objc', 'AntlrObjectiveC'),
        ('antlr-perl', 'AntlrPerl'),
        ('antlr-python', 'AntlrPython'),
        ('antlr-ruby', 'AntlrRuby'),
        ('ebnf', 'Ebnf'),
        ('ragel-c', 'RagelC'),
        ('ragel-cpp', 'RagelCpp'),
        ('ragel-d', 'RagelD'),
        ('ragel-em', 'RagelEmbedded'),
        ('ragel-java', 'RagelJava'),
        ('ragel', 'Ragel'),
        ('ragel-objc', 'RagelObjectiveC'),
        ('ragel-ruby', 'RagelRuby'),
        ('treetop', 'Treetop'),
        ('ada', 'Ada'),
        ('delphi', 'Delphi'),
        ('pawn', 'Pawn'),
        ('sp', 'SourcePawn'),
        ('perl6', 'Perl6'),
        ('perl', 'Perl'),
        ('php', 'Php'),
        ('zephir', 'Zephir'),
        ('praat', 'Praat'),
        ('logtalk', 'Logtalk'),
        ('prolog', 'Prolog'),
        ('cython', 'Cython'),
        ('dg', 'Dg'),
        ('numpy', 'NumPy'),
        ('python3', 'Python3'),
        ('py3tb', 'Python3Traceback'),
        ('pycon', 'PythonConsole'),
        ('python', 'Python'),
        ('pytb', 'PythonTraceback'),
        ('qvto', 'QVTo'),
        ('rconsole', 'RConsole'),
        ('rd', 'Rd'),
        ('splus', 'S'),
        ('sparql', 'Sparql'),
        ('turtle', 'Turtle'),
        ('rebol', 'Rebol'),
        ('red', 'Red'),
        ('resource', 'Resource'),
        ('rnc', 'RNCCompact'),
        ('roboconf-graph', 'RoboconfGraph'),
        ('roboconf-instances', 'RoboconfInstances'),
        ('robotframework', 'RobotFramework'),
        ('fancy', 'Fancy'),
        ('rbcon', 'RubyConsole'),
        ('rb', 'Ruby'),
        ('rust', 'Rust'),
        ('sas', 'SAS'),
        ('applescript', 'AppleScript'),
        ('chai', 'Chaiscript'),
        ('easytrieve', 'Easytrieve'),
        ('hybris', 'Hybris'),
        ('jcl', 'Jcl'),
        ('lsl', 'LSL'),
        ('lua', 'Lua'),
        ('moocode', 'MOOCode'),
        ('moon', 'MoonScript'),
        ('rexx', 'Rexx'),
        ('bash', 'Bash'),
        ('console', 'BashSession'),
        ('bat', 'Batch'),
        ('fish', 'FishShell'),
        ('doscon', 'MSDOSSession'),
        ('powershell', 'PowerShell'),
        ('ps1con', 'PowerShellSession'),
        ('tcsh', 'Tcsh'),
        ('tcshcon', 'TcshSession'),
        ('newspeak', 'Newspeak'),
        ('smalltalk', 'Smalltalk'),
        ('nusmv', 'NuSMV'),
        ('snobol', 'Snobol'),
        ('raw', 'RawToken'),
        ('mysql', 'MySql'),
        ('plpgsql', 'PlPgsql'),
        ('psql', 'PostgresConsole'),
        ('postgresql', 'Postgres'),
        ('rql', 'Rql'),
        ('sql', 'Sql'),
        ('sqlite3', 'SqliteConsole'),
        ('tsql', 'TransactSql'),
        ('stata', 'Stata'),
        ('sc', 'SuperCollider'),
        ('tcl', 'Tcl'),
        ('html+ng2', 'Angular2Html'),
        ('ng2', 'Angular2'),
        ('html+cheetah', 'CheetahHtml'),
        ('js+cheetah', 'CheetahJavascript'),
        ('cheetah', 'Cheetah'),
        ('xml+cheetah', 'CheetahXml'),
        ('cfc', 'ColdfusionCFC'),
        ('cfm', 'ColdfusionHtml'),
        ('cfs', 'Coldfusion'),
        ('css+django', 'CssDjango'),
        ('css+erb', 'CssErb'),
        ('css+genshitext', 'CssGenshi'),
        ('css+php', 'CssPhp'),
        ('css+smarty', 'CssSmarty'),
        ('django', 'Django'),
        ('erb', 'Erb'),
        ('html+evoque', 'EvoqueHtml'),
        ('evoque', 'Evoque'),
        ('xml+evoque', 'EvoqueXml'),
        ('genshi', 'Genshi'),
        ('genshitext', 'GenshiText'),
        ('html+handlebars', 'HandlebarsHtml'),
        ('handlebars', 'Handlebars'),
        ('html+django', 'HtmlDjango'),
        ('html+genshi', 'HtmlGenshi'),
        ('html+php', 'HtmlPhp'),
        ('html+smarty', 'HtmlSmarty'),
        ('js+django', 'JavascriptDjango'),
        ('js+erb', 'JavascriptErb'),
        ('js+genshitext', 'JavascriptGenshi'),
        ('js+php', 'JavascriptPhp'),
        ('js+smarty', 'JavascriptSmarty'),
        ('jsp', 'Jsp'),
        ('css+lasso', 'LassoCss'),
        ('html+lasso', 'LassoHtml'),
        ('js+lasso', 'LassoJavascript'),
        ('xml+lasso', 'LassoXml'),
        ('liquid', 'Liquid'),
        ('css+mako', 'MakoCss'),
        ('html+mako', 'MakoHtml'),
        ('js+mako', 'MakoJavascript'),
        ('mako', 'Mako'),
        ('xml+mako', 'MakoXml'),
        ('mason', 'Mason'),
        ('css+myghty', 'MyghtyCss'),
        ('html+myghty', 'MyghtyHtml'),
        ('js+myghty', 'MyghtyJavascript'),
        ('myghty', 'Myghty'),
        ('xml+myghty', 'MyghtyXml'),
        ('rhtml', 'Rhtml'),
        ('smarty', 'Smarty'),
        ('ssp', 'Ssp'),
        ('tea', 'TeaTemplate'),
        ('html+twig', 'TwigHtml'),
        ('twig', 'Twig'),
        ('html+velocity', 'VelocityHtml'),
        ('velocity', 'Velocity'),
        ('xml+velocity', 'VelocityXml'),
        ('xml+django', 'XmlDjango'),
        ('xml+erb', 'XmlErb'),
        ('xml+php', 'XmlPhp'),
        ('xml+smarty', 'XmlSmarty'),
        ('yaml+jinja', 'YamlJinja'),
        ('cucumber', 'Gherkin'),
        ('tap', 'TAP'),
        ('awk', 'Awk'),
        ('vim', 'Vim'),
        ('pot', 'Gettext'),
        ('http', 'Http'),
        ('irc', 'IrcLogs'),
        ('todotxt', 'Todotxt'),
        ('coq', 'Coq'),
        ('isabelle', 'Isabelle'),
        ('lean', 'Lean'),
        ('rts', 'Rts'),
        ('typoscriptcssdata', 'TypoScriptCssData'),
        ('typoscripthtmldata', 'TypoScriptHtmlData'),
        ('typoscript', 'TypoScript'),
        ('urbiscript', 'Urbiscript'),
        ('vcl', 'VCL'),
        ('vclsnippets', 'VCLSnippet'),
        ('boogie', 'Boogie'),
        ('silver', 'Silver'),
        ('cirru', 'Cirru'),
        ('duel', 'Duel'),
        ('qml', 'Qml'),
        ('slim', 'Slim'),
        ('xquery', 'XQuery'),
        ('whiley', 'Whiley'),
        ('x10', 'X10'),
        ('xorg.conf', 'Xorg'),
    )
     ),
    ('ActionScript and MXML', (
        ('as3', 'ActionScript3'),
        ('as', 'ActionScript'),
        ('mxml', 'Mxml'),
    )
     ),
    ('computer algebra systems', (
        ('bc', 'BC'),
        ('gap', 'GAP'),
        ('mathematica', 'Mathematica'),
        ('mupad', 'MuPAD'),
    )
     ),
    ('AmbientTalk language', (
        ('at', 'AmbientTalk'),
    )
     ),
    ('AMPL language', (
        ('ampl', 'Ampl'),
    )
     ),
    ('APL', (
        ('apl', 'APL'),
    )
     ),
    ('Archetype-related syntaxes, including:', (
        ('adl', 'Adl'),
        ('cadl', 'Cadl'),
        ('odin', 'Odin'),
    )
     ),
    ('assembly languages', (
        ('c-objdump', 'CObjdump'),
        ('ca65', 'Ca65'),
        ('cpp-objdump', 'CppObjdump'),
        ('d-objdump', 'DObjdump'),
        ('gas', 'Gas'),
        ('hsail', 'Hsail'),
        ('llvm', 'Llvm'),
        ('nasm', 'Nasm'),
        ('objdump-nasm', 'NasmObjdump'),
        ('objdump', 'Objdump'),
        ('tasm', 'Tasm'),
    )
     ),
    ('automation scripting languages', (
        ('autoit', 'AutoIt'),
        ('ahk', 'Autohotkey'),
    )
     ),
    ('BASIC like languages (other than VB.net)', (
        ('blitzbasic', 'BlitzBasic'),
        ('blitzmax', 'BlitzMax'),
        ('cbmbas', 'CbmBasicV2'),
        ('monkey', 'Monkey'),
        ('qbasic', 'QBasic'),
    )
     ),
    ('BibTeX bibliography data and styles', (
        ('bst', 'BST'),
        ('bib', 'BibTeX'),
    )
     ),
    ('“business-oriented” languages', (
        ('abap', 'ABAP'),
        ('cobolfree', 'CobolFreeformat'),
        ('cobol', 'Cobol'),
        ('gooddata-cl', 'GoodDataCL'),
        ('maql', 'Maql'),
        ('openedge', 'OpenEdge'),
    )
     ),
    ('C/C++ languages', (
        ('c', 'C'),
        ('cpp', 'Cpp'),
    )
     ),
    ('other C-like languages', (
        ('arduino', 'Arduino'),
        ('clay', 'Clay'),
        ('cuda', 'Cuda'),
        ('ec', 'EC'),
        ('mql', 'Mql'),
        ('nesc', 'NesC'),
        ('pike', 'Pike'),
        ('swig', 'Swig'),
        ('vala', 'Vala'),
    )
     ),
    ('Cap’n Proto schema language', (
        ('capnp', 'CapnProto'),
    )
     ),
    ('Chapel language', (
        ('chapel', 'Chapel'),
    )
     ),
    ('Clean language', (
        ('clean', 'Clean'),
    )
     ),
    ('configuration file formats', (
        ('apacheconf', 'ApacheConf'),
        ('cfengine3', 'Cfengine3'),
        ('docker', 'Docker'),
        ('ini', 'Ini'),
        ('kconfig', 'Kconfig'),
        ('lighty', 'LighttpdConf'),
        ('nginx', 'NginxConf'),
        ('pacmanconf', 'PacmanConf'),
        ('pkgconfig', 'PkgConfig'),
        ('properties', 'Properties'),
        ('registry', 'Regedit'),
        ('squidconf', 'SquidConf'),
        ('termcap', 'Termcap'),
        ('terminfo', 'Terminfo'),
        ('terraform', 'Terraform'),
    )
     ),
    ('misc console output', (
        ('pypylog', 'PyPyLog'),
        ('vctreestatus', 'VCTreeStatus'),
    )
     ),
    ('Crystal', (
        ('cr', 'Crystal'),
    )
     ),
    ('Csound languages', (
        ('csound-document', 'CsoundDocument'),
        ('csound', 'CsoundOrchestra'),
        ('csound-score', 'CsoundScore'),
    )
     ),
    ('CSS and related stylesheet formats', (
        ('css', 'Css'),
        ('less', 'LessCss'),
        ('sass', 'Sass'),
        ('scss', 'Scss'),
    )
     ),
    ('D languages', (
        ('croc', 'Croc'),
        ('d', 'D'),
        ('minid', 'MiniD'),
    )
     ),
    ('Pygments lexers for Dalvik VM-related languages', (
        ('smali', 'Smali'),
    )
     ),
    ('data file format', (
        ('json-object', 'JsonBareObject'),
        ('jsonld', 'JsonLd'),
        ('json', 'Json'),
        ('yaml', 'Yaml'),
    )
     ),
    ('diff/patch formats', (
        ('dpatch', 'DarcsPatch'),
        ('diff', 'Diff'),
        ('wdiff', 'WDiff'),
    )
     ),
    ('.net languages', (
        ('boo', 'Boo'),
        ('aspx-cs', 'CSharpAspx'),
        ('csharp', 'CSharp'),
        ('fsharp', 'FSharp'),
        ('nemerle', 'Nemerle'),
        ('aspx-vb', 'VbNetAspx'),
        ('vb.net', 'VbNet'),
    )
     ),
    ('various domain-specific languages', (
        ('alloy', 'Alloy'),
        ('bro', 'Bro'),
        ('crmsh', 'Crmsh'),
        ('flatline', 'Flatline'),
        ('mscgen', 'Mscgen'),
        ('pan', 'Pan'),
        ('protobuf', 'ProtoBuf'),
        ('puppet', 'Puppet'),
        ('rsl', 'Rsl'),
        ('snowball', 'Snowball'),
        ('thrift', 'Thrift'),
        ('vgl', 'VGL'),
    )
     ),
    ('Dylan language', (
        ('dylan-console', 'DylanConsole'),
        ('dylan', 'Dylan'),
        ('dylan-lid', 'DylanLid'),
    )
     ),
    ('ECL language', (
        ('ecl', 'ECL'),
    )
     ),
    ('Eiffel language', (
        ('eiffel', 'Eiffel'),
    )
     ),
    ('Elm programming language', (
        ('elm', 'Elm'),
    )
     ),
    ('Erlang', (
        ('iex', 'ElixirConsole'),
        ('elixir', 'Elixir'),
        ('erlang', 'Erlang'),
        ('erl', 'ErlangShell'),
    )
     ),
    ('esoteric languages', (
        ('aheui', 'Aheui'),
        ('befunge', 'Befunge'),
        ('brainfuck', 'Brainfuck'),
        ('camkes', 'CAmkES'),
        ('capdl', 'CapDL'),
        ('redcode', 'Redcode'),
    )
     ),
    ('Pygments lexers for Ezhil language', (
        ('ezhil', 'Ezhil'),
    )
     ),
    ('Factor language', (
        ('factor', 'Factor'),
    )
     ),
    ('Fantom language', (
        ('fan', 'Fantom'),
    )
     ),
    ('Felix language', (
        ('felix', 'Felix'),
    )
     ),
    ('FloScript', (
        ('floscript', 'FloScript'),
    )
     ),
    ('Forth language', (
        ('forth', 'Forth'),
    )
     ),
    ('Fortran languages', (
        ('fortranfixed', 'FortranFixed'),
        ('fortran', 'Fortran'),
    )
     ),
    ('Simple lexer for Microsoft Visual FoxPro source code', (
        ('foxpro', 'FoxPro'),
    )
     ),
    ('Google Go language', (
        ('go', 'Go'),
    )
     ),
    ('grammer notations like BNF', (
        ('abnf', 'Abnf'),
        ('bnf', 'Bnf'),
        ('jsgf', 'Jsgf'),
    )
     ),
    ('graph query languages', (
        ('cypher', 'Cypher'),
    )
     ),
    ('computer graphics and plotting related languages', (
        ('asy', 'Asymptote'),
        ('glsl', 'GLShader'),
        ('gnuplot', 'Gnuplot'),
        ('hlsl', 'HLSLShader'),
        ('postscript', 'PostScript'),
        ('pov', 'Povray'),
    )
     ),
    ('Haskell and related languages', (
        ('agda', 'Agda'),
        ('cryptol', 'Cryptol'),
        ('haskell', 'Haskell'),
        ('idris', 'Idris'),
        ('koka', 'Koka'),
        ('lagda', 'LiterateAgda'),
        ('lcry', 'LiterateCryptol'),
        ('lhs', 'LiterateHaskell'),
        ('lidr', 'LiterateIdris'),
    )
     ),
    ('Haxe and related stuff', (
        ('hx', 'Haxe'),
        ('haxeml', 'Hxml'),
    )
     ),
    ('hardware descriptor languages', (
        ('systemverilog', 'SystemVerilog'),
        ('verilog', 'Verilog'),
        ('vhdl', 'Vhdl'),
    )
     ),
    ('hexadecimal dumps', (
        ('hexdump', 'Hexdump'),
    )
     ),
    ('HTML, XML and related markup', (
        ('dtd', 'Dtd'),
        ('haml', 'Haml'),
        ('html', 'Html'),
        ('pug', 'Pug'),
        ('scaml', 'Scaml'),
        ('xml', 'Xml'),
        ('xslt', 'Xslt'),
    )
     ),
    ('IDL', (
        ('idl', 'IDL'),
    )
     ),
    ('Igor Pro', (
        ('igor', 'Igor'),
    )
     ),
    ('Inferno os and all the related stuff', (
        ('limbo', 'Limbo'),
    )
     ),
    ('installer/packager DSLs and formats', (
        ('control', 'DebianControl'),
        ('nsis', 'NSIS'),
        ('spec', 'RPMSpec'),
        ('sourceslist', 'SourcesList'),
    )
     ),
    ('interactive fiction languages', (
        ('inform6', 'Inform6'),
        ('i6t', 'Inform6Template'),
        ('inform7', 'Inform7'),
        ('tads3', 'Tads3'),
    )
     ),
    ('Io language', (
        ('io', 'Io'),
    )
     ),
    ('J programming language', (
        ('j', 'J'),
    )
     ),
    ('JavaScript and related languages', (
        ('coffee-script', 'CoffeeScript'),
        ('dart', 'Dart'),
        ('earl-grey', 'EarlGrey'),
        ('js', 'Javascript'),
        ('juttle', 'Juttle'),
        ('kal', 'Kal'),
        ('lasso', 'Lasso'),
        ('live-script', 'LiveScript'),
        ('mask', 'Mask'),
        ('objective-j', 'ObjectiveJ'),
        ('ts', 'TypeScript'),
    )
     ),
    ('Julia language', (
        ('jlcon', 'JuliaConsole'),
        ('julia', 'Julia'),
    )
     ),
    ('Pygments lexers for JVM languages', (
        ('aspectj', 'AspectJ'),
        ('ceylon', 'Ceylon'),
        ('clojure', 'Clojure'),
        ('clojurescript', 'ClojureScript'),
        ('golo', 'Golo'),
        ('gosu', 'Gosu'),
        ('gst', 'GosuTemplate'),
        ('groovy', 'Groovy'),
        ('ioke', 'Ioke'),
        ('jasmin', 'Jasmin'),
        ('java', 'Java'),
        ('kotlin', 'Kotlin'),
        ('pig', 'Pig'),
        ('sarl', 'Sarl'),
        ('scala', 'Scala'),
        ('xtend', 'Xtend'),
    )
     ),
    ('Lispy languages', (
        ('cpsa', 'CPSA'),
        ('common-lisp', 'CommonLisp'),
        ('emacs', 'EmacsLisp'),
        ('fennel', 'Fennel'),
        ('hylang', 'Hy'),
        ('newlisp', 'NewLisp'),
        ('racket', 'Racket'),
        ('scheme', 'Scheme'),
        ('shen', 'Shen'),
        ('extempore', 'Xtlang'),
    )
     ),
    ('Makefiles and similar', (
        ('basemake', 'BaseMakefile'),
        ('cmake', 'CMake'),
        ('make', 'Makefile'),
    )
     ),
    ('non-HTML markup languages', (
        ('bbcode', 'BBCode'),
        ('groff', 'Groff'),
        ('md', 'Markdown'),
        ('trac-wiki', 'MoinWiki'),
        ('css+mozpreproc', 'MozPreprocCss'),
        ('mozhashpreproc', 'MozPreprocHash'),
        ('javascript+mozpreproc', 'MozPreprocJavascript'),
        ('mozpercentpreproc', 'MozPreprocPercent'),
        ('xul+mozpreproc', 'MozPreprocXul'),
        ('rst', 'Rst'),
        ('tex', 'Tex'),
    )
     ),
    ('Matlab and related languages', (
        ('matlab', 'Matlab'),
        ('matlabsession', 'MatlabSession'),
        ('octave', 'Octave'),
        ('scilab', 'Scilab'),
    )
     ),
    ('ML family languages', (
        ('ocaml', 'Ocaml'),
        ('opa', 'Opa'),
        ('sml', 'SML'),
    )
     ),
    ('modeling languages', (
        ('bugs', 'Bugs'),
        ('jags', 'Jags'),
        ('modelica', 'Modelica'),
        ('stan', 'Stan'),
    )
     ),
    ('Multi-Dialect Modula-2', (
        ('modula2', 'Modula2'),
    )
     ),
    ('Monte programming language', (
        ('monte', 'Monte'),
    )
     ),
    ('NCAR Command Language', (
        ('ncl', 'NCL'),
    )
     ),
    ('Nim language (formerly known as Nimrod)', (
        ('nim', 'Nimrod'),
    )
     ),
    ('Nit language', (
        ('nit', 'Nit'),
    )
     ),
    ('NixOS Nix language', (
        ('nixos', 'Nix'),
    )
     ),
    ('Oberon family languages', (
        ('componentpascal', 'ComponentPascal'),
    )
     ),
    ('Objective-C family languages', (
        ('logos', 'Logos'),
        ('objective-c', 'ObjectiveC'),
        ('objective-c++', 'ObjectiveCpp'),
        ('swift', 'Swift'),
    )
     ),
    ('Ooc language', (
        ('ooc', 'Ooc'),
    )
     ),
    ('ParaSail', (
        ('parasail', 'ParaSail'),
    )
     ),
    ('parser generators', (
        ('antlr-as', 'AntlrActionScript'),
        ('antlr-csharp', 'AntlrCSharp'),
        ('antlr-cpp', 'AntlrCpp'),
        ('antlr-java', 'AntlrJava'),
        ('antlr', 'Antlr'),
        ('antlr-objc', 'AntlrObjectiveC'),
        ('antlr-perl', 'AntlrPerl'),
        ('antlr-python', 'AntlrPython'),
        ('antlr-ruby', 'AntlrRuby'),
        ('ebnf', 'Ebnf'),
        ('ragel-c', 'RagelC'),
        ('ragel-cpp', 'RagelCpp'),
        ('ragel-d', 'RagelD'),
        ('ragel-em', 'RagelEmbedded'),
        ('ragel-java', 'RagelJava'),
        ('ragel', 'Ragel'),
        ('ragel-objc', 'RagelObjectiveC'),
        ('ragel-ruby', 'RagelRuby'),
        ('treetop', 'Treetop'),
    )
     ),
    ('Pascal family languages', (
        ('ada', 'Ada'),
        ('delphi', 'Delphi'),
    )
     ),
    ('Pawn languages', (
        ('pawn', 'Pawn'),
        ('sp', 'SourcePawn'),
    )
     ),
    ('Perl and related languages', (
        ('perl6', 'Perl6'),
        ('perl', 'Perl'),
    )
     ),
    ('PHP and related languages', (
        ('php', 'Php'),
        ('zephir', 'Zephir'),
    )
     ),
    ('Praat', (
        ('praat', 'Praat'),
    )
     ),
    ('Prolog and Prolog-like languages', (
        ('logtalk', 'Logtalk'),
        ('prolog', 'Prolog'),
    )
     ),
    ('Python and related languages', (
        ('cython', 'Cython'),
        ('dg', 'Dg'),
        ('numpy', 'NumPy'),
        ('python3', 'Python3'),
        ('py3tb', 'Python3Traceback'),
        ('pycon', 'PythonConsole'),
        ('python', 'Python'),
        ('pytb', 'PythonTraceback'),
    )
     ),
    ('QVT Operational language', (
        ('qvto', 'QVTo'),
    )
     ),
    ('R/S languages', (
        ('rconsole', 'RConsole'),
        ('rd', 'Rd'),
        ('splus', 'S'),
    )
     ),
    ('semantic web and RDF query languages and markup', (
        ('sparql', 'Sparql'),
        ('turtle', 'Turtle'),
    )
     ),
    ('REBOL and related languages', (
        ('rebol', 'Rebol'),
        ('red', 'Red'),
    )
     ),
    ('resource definition files', (
        ('resource', 'Resource'),
    )
     ),
    ('Relax-NG Compact syntax', (
        ('rnc', 'RNCCompact'),
    )
     ),
    ('Roboconf DSL', (
        ('roboconf-graph', 'RoboconfGraph'),
        ('roboconf-instances', 'RoboconfInstances'),
    )
     ),
    ('Robot Framework', (
        ('robotframework', 'RobotFramework'),
    )
     ),
    ('Ruby and related languages', (
        ('fancy', 'Fancy'),
        ('rbcon', 'RubyConsole'),
        ('rb', 'Ruby'),
    )
     ),
    ('Rust language', (
        ('rust', 'Rust'),
    )
     ),
    ('SAS', (
        ('sas', 'SAS'),
    )
     ),
    ('scripting and embedded languages', (
        ('applescript', 'AppleScript'),
        ('chai', 'Chaiscript'),
        ('easytrieve', 'Easytrieve'),
        ('hybris', 'Hybris'),
        ('jcl', 'Jcl'),
        ('lsl', 'LSL'),
        ('lua', 'Lua'),
        ('moocode', 'MOOCode'),
        ('moon', 'MoonScript'),
        ('rexx', 'Rexx'),
    )
     ),
    ('various shells', (
        ('bash', 'Bash'),
        ('console', 'BashSession'),
        ('bat', 'Batch'),
        ('fish', 'FishShell'),
        ('doscon', 'MSDOSSession'),
        ('powershell', 'PowerShell'),
        ('ps1con', 'PowerShellSession'),
        ('tcsh', 'Tcsh'),
        ('tcshcon', 'TcshSession'),
    )
     ),
    ('Smalltalk and related languages', (
        ('newspeak', 'Newspeak'),
        ('smalltalk', 'Smalltalk'),
    )
     ),
    ('SMV languages', (
        ('nusmv', 'NuSMV'),
    )
     ),
    ('SNOBOL language', (
        ('snobol', 'Snobol'),
    )
     ),
    ('Special lexers', (
        ('raw', 'RawToken'),
        ('text', 'Text'),
    )
     ),
    ('various SQL dialects and related interactive sessions', (
        ('mysql', 'MySql'),
        ('plpgsql', 'PlPgsql'),
        ('psql', 'PostgresConsole'),
        ('postgresql', 'Postgres'),
        ('rql', 'Rql'),
        ('sql', 'Sql'),
        ('sqlite3', 'SqliteConsole'),
        ('tsql', 'TransactSql'),
    )
     ),
    ('Stata', (
        ('stata', 'Stata'),
    )
     ),
    ('SuperCollider', (
        ('sc', 'SuperCollider'),
    )
     ),
    ('Tcl and related languages', (
        ('tcl', 'Tcl'),
    )
     ),
    ('various template engines’ markup', (
        ('html+ng2', 'Angular2Html'),
        ('ng2', 'Angular2'),
        ('html+cheetah', 'CheetahHtml'),
        ('js+cheetah', 'CheetahJavascript'),
        ('cheetah', 'Cheetah'),
        ('xml+cheetah', 'CheetahXml'),
        ('cfc', 'ColdfusionCFC'),
        ('cfm', 'ColdfusionHtml'),
        ('cfs', 'Coldfusion'),
        ('css+django', 'CssDjango'),
        ('css+erb', 'CssErb'),
        ('css+genshitext', 'CssGenshi'),
        ('css+php', 'CssPhp'),
        ('css+smarty', 'CssSmarty'),
        ('django', 'Django'),
        ('erb', 'Erb'),
        ('html+evoque', 'EvoqueHtml'),
        ('evoque', 'Evoque'),
        ('xml+evoque', 'EvoqueXml'),
        ('genshi', 'Genshi'),
        ('genshitext', 'GenshiText'),
        ('html+handlebars', 'HandlebarsHtml'),
        ('handlebars', 'Handlebars'),
        ('html+django', 'HtmlDjango'),
        ('html+genshi', 'HtmlGenshi'),
        ('html+php', 'HtmlPhp'),
        ('html+smarty', 'HtmlSmarty'),
        ('js+django', 'JavascriptDjango'),
        ('js+erb', 'JavascriptErb'),
        ('js+genshitext', 'JavascriptGenshi'),
        ('js+php', 'JavascriptPhp'),
        ('js+smarty', 'JavascriptSmarty'),
        ('jsp', 'Jsp'),
        ('css+lasso', 'LassoCss'),
        ('html+lasso', 'LassoHtml'),
        ('js+lasso', 'LassoJavascript'),
        ('xml+lasso', 'LassoXml'),
        ('liquid', 'Liquid'),
        ('css+mako', 'MakoCss'),
        ('html+mako', 'MakoHtml'),
        ('js+mako', 'MakoJavascript'),
        ('mako', 'Mako'),
        ('xml+mako', 'MakoXml'),
        ('mason', 'Mason'),
        ('css+myghty', 'MyghtyCss'),
        ('html+myghty', 'MyghtyHtml'),
        ('js+myghty', 'MyghtyJavascript'),
        ('myghty', 'Myghty'),
        ('xml+myghty', 'MyghtyXml'),
        ('rhtml', 'Rhtml'),
        ('smarty', 'Smarty'),
        ('ssp', 'Ssp'),
        ('tea', 'TeaTemplate'),
        ('html+twig', 'TwigHtml'),
        ('twig', 'Twig'),
        ('html+velocity', 'VelocityHtml'),
        ('velocity', 'Velocity'),
        ('xml+velocity', 'VelocityXml'),
        ('xml+django', 'XmlDjango'),
        ('xml+erb', 'XmlErb'),
        ('xml+php', 'XmlPhp'),
        ('xml+smarty', 'XmlSmarty'),
        ('yaml+jinja', 'YamlJinja'),
    )
     ),
    ('testing languages', (
        ('cucumber', 'Gherkin'),
        ('tap', 'TAP'),
    )
     ),
    ('languages related to text processing', (
        ('awk', 'Awk'),
        ('vim', 'Vim'),
    )
     ),
    ('various text formats', (
        ('pot', 'Gettext'),
        ('http', 'Http'),
        ('irc', 'IrcLogs'),
        ('todotxt', 'Todotxt'),
    )
     ),
    ('orem-proving languages', (
        ('coq', 'Coq'),
        ('isabelle', 'Isabelle'),
        ('lean', 'Lean'),
    )
     ),
    ('RiverBed’s TrafficScript (RTS) language', (
        ('rts', 'Rts'),
    )
     ),
    ('TypoScript', (
        ('typoscriptcssdata', 'TypoScriptCssData'),
        ('typoscripthtmldata', 'TypoScriptHtmlData'),
        ('typoscript', 'TypoScript'),
    )
     ),
    ('UrbiScript language', (
        ('urbiscript', 'Urbiscript'),
    )
     ),
    ('Varnish configuration', (
        ('vcl', 'VCL'),
        ('vclsnippets', 'VCLSnippet'),
    )
     ),
    ('Intermediate Verification Languages (IVLs)', (
        ('boogie', 'Boogie'),
        ('silver', 'Silver'),
    )
     ),
    ('misc. web stuff', (
        ('cirru', 'Cirru'),
        ('duel', 'Duel'),
        ('qml', 'Qml'),
        ('slim', 'Slim'),
        ('xquery', 'XQuery'),
    )
     ),
    ('Whiley language', (
        ('whiley', 'Whiley'),
    )
     ),
    ('X10 programming language', (
        ('x10', 'X10'),
    )
     ),
    ('Xorg configs', (
        ('xorg.conf', 'Xorg'),
    )
     ),
    ('Iterating over all lexers', (
    )
     ),
)

EXPIRED = {
    '10M': {
        'name': '10 Minutes',
        'time': 600
    },
    '1H': {
        'name': '1 Hour',
        'time': 3600
    },
    '1D': {
        'name': '1 Day',
        'time': 86400
    },
    '1W': {
        'name': '1 Week',
        'time': 604800
    },
    '2W': {
        'name': '2 Weeks',
        'time': 1209600
    },
    '1M': {
        'name': '1 Month',
        'time': 2592000
    },
    '6M': {
        'name': '6 Months',
        'time': 15768000
    },
    '1Y': {
        'name': '1 Year',
        'time': 31536000
    }
}

EXPIRED = getattr(settings, 'EXPIRED', EXPIRED)

EXPIRED_CHOICE = ((item, EXPIRED[item]['name']) for item in EXPIRED)

EXPIRED_DEFAULT = getattr(settings, 'EXPIRED_DEFAULT', '10M')

LANGUAGE_CHOICE = getattr(settings, 'LANGUAGE', LANGUAGE)

LANGUAGE_DEFAULT = getattr(settings, 'EXPIRED_DEFAULT', 'Text')
