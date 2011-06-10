set ignorecase
set smartcase
set incsearch
set tabstop=4
set shiftwidth=4
set expandtab
syntax on
set viminfo='10,\"100,:20,%,n~/.viminfo
    au BufReadPost * if line("'\"") > 0|if line("'\"") <= line("$")|exe("norm '\"")|else|exe "norm
$"|endif|endif
set hlsearch
set hlsearch
