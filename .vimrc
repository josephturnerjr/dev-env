runtime bundle/vim-pathogen/autoload/pathogen.vim
call pathogen#infect()
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
highlight MatchParen ctermbg=4
nnoremap <silent> <C-t> :tabnew<CR>
nnoremap <silent> :gt :tabnext<CR>
set ruler
let syntastic_check_on_open = 1
let syntastic_enable_signs = 1
let syntastic_mode_map = { 'mode': 'passive', 'active_filetypes': ['python']}
set backspace=2
nnoremap <esc> :noh<return><esc>
