# latexmk configuration for this thesis template.
#   latexmk main.tex          -> builds the PDF with XeLaTeX
#   latexmk -c                -> removes auxiliary files
#   latexmk -C                -> removes auxiliary files and the PDF

$pdf_mode = 5;          # 5 = xelatex
$bibtex_use = 2;        # run bibtex, and clean the .bbl on latexmk -C
$out_dir = 'build';

# Build the nomenclature (.nlo -> .nls) via makeindex.
add_cus_dep('nlo', 'nls', 0, 'makenlo2nls');
sub makenlo2nls {
    system("makeindex -s nomencl.ist -o \"$_[0].nls\" \"$_[0].nlo\"");
}

# Build the index (.idx -> .ind).
add_cus_dep('idx', 'ind', 0, 'makeidx2ind');
sub makeidx2ind {
    system("makeindex -o \"$_[0].ind\" \"$_[0].idx\"");
}

push @generated_exts, 'nlo', 'nls', 'ind', 'idx', 'ilg', 'acn', 'acr', 'alg';
