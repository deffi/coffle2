General
=======

General notes:
  * A directory cannot be simultaneously a coffle repository and a coffle target
  * All commands are intended to be run in the target or in a subdirectory of a
    target
  * The repository is not modified (no state in the repository). Thus, a
    repository can be installed to multiple targets (e. g. for multiple users).
    Also, repos may be read-only and the target should not break if the repo is
    deleted or otherwise unavailable.


Repo
====

Repo:
    .coffle/
        repository.toml

repository.toml:
  * version


Target
======

Target:
    .coffle_target/
        state.json
        repo ->
        backup/ ?
        org/ ?
        output/ ?

state.json:
  * Version
  * For each entry:
    * skipped with timestamp


Future work
===========

Additional features:
  * Set the file mode
  * Set the directory mode
  * Install multiple repos to a target (see below)
  * Different files in the repo (one is selected at build time) for the same
    target file
  * Files in a repo include other files? How do we prevent them from being
    generated individually?
  * Include whole other repos? Probably not because we wouldn't want to store
    the location of one repo in another; it may be checked out in a different
    location. Installing multiple repos in the same target probably covers the
    use cases better. 

Installing multiple repos to a target:
  * As long as we only have one, use simpler commands
  * We probably need an install order
  * State in the target is mostly per-repo
  * Files should be able to specify "skip" (file from previous repo is
    installed) or "suppress" (no file is installed, even if a previous repo had
    one)
  * Content from multiple repos for the same file:
    * Concatenate?
    * Postprocess?
    * Install under different names so one can be sourced from the other
