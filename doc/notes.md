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


Operations
  * Install
    * Builds first, where required
    * Optionally overwrites (with backup) existing entries
  * Uninstall
    * Restores backups where they exist
    * Removes directories that are now empty? Store in target state whether the
      directory was empty before install?
  * Edit
    * Edits the corresponding file in the repo
    * Re-builds the entry
  * Status
    * Status of all installed files? All files in the repo?
  * Build
  * Info
  * Diff
  * Merge
  * Init or repo init?

Changes from version 1:
  * We don't treat directories as entries
  * State goes into the target, in into the repository




Repo
====

Repo layout:
    .coffle/
        repository.toml
    **/
        file
        _.dotfile
        .coffleignore  - also a template

repository.toml:
  * version

Open questions:
  * Configuring the template engine - maybe per file?
  * Should .coffleignore use regular expressions or glob patterns?
    * Pro regex:
      * More powerful
      * Selectable case sensitivity?
    * Pro glob:
      * Like .gitignore
      * Easier to distinguish between "here" and "here and in subirectories"?
    * Switchable?
      * / might conflict with "this directory"

Target
======

Target:
    .coffle/
        target.json
        repo ->
        backup/ ?
        build/ ?
        install/ ?

target.json:
  * Version
  * For each entry:
    * skipped with timestamp


Future work
===========

Additional features:
  * Host-specific files in repo? - easier than large host() blocks
  * Local files to be included (!) into the generated file? 
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
  * Backup, build, and install: per target or per target+repo? 
  * Files should be able to specify "skip" (file from previous repo is
    installed) or "suppress" (no file is installed, even if a previous repo had
    one)
  * Content from multiple repos for the same file:
    * Concatenate?
    * Postprocess?
    * Install under different names so one can be sourced from the other
      * "Previous" link for every repo, with the link of the first pointing to
        the backup?
