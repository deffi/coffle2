Repo:
  * Unescaping should be part of the repo, not part of the target.
    If we change the escaping scheme, we have to change the repo
    It interacts with what files (dotfiles) we ignore in the repo
    * Repo entries need a path to the original file, and the relative path
      should already be unescaped
  * Check for duplicate names (post-unescape)
  * Can't have an entry called _coffle (for .coffle) because we will be
    using that name
