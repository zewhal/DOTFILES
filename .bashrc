#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
git_branch() {
    branch=$(git symbolic-ref --short HEAD 2>/dev/null)
    if [ -n "$branch" ]; then
        echo "[$branch]"
    fi
}

PS1='\u@\h:\w$(git_branch)\n> '
. "$HOME/.cargo/env"

. "$HOME/.local/bin/env"
