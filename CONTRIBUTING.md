## Submitting a Pull Request

Good pull requests, whether patches, improvements, or new features, are a fantastic help. They should remain focused in scope and avoid containing unrelated commits.

**Please ask first** before embarking on any significant pull requests (e.g. implementing features, refactoring code), otherwise you risk spending a lot of time working on something that the project's developers might not want to merge into the project.

If you have never created a pull request before, welcome 🎉 😄. [Here is a great tutorial](https://opensource.guide/how-to-contribute/#opening-a-pull-request) on how to send one :)

Here is a summary of the steps to follow:

1. Always get the latest changes from upstream and update dependencies:
```bash
$ git checkout main
$ git pull -r upstream main
$ npm install
```
2. Create a new topic branch (off the main project development branch) to contain your feature, change, or fix:
```bash
$ git checkout -b <topic-branch-name>
```
3. Make your code changes, following the [Coding rules](#coding-rules)
4. Push your topic branch up to your fork:
```bash
$ git push --set-u origin <topic-branch-name>
```
5. [Open a Pull Request](https://help.github.com/articles/creating-a-pull-request/#creating-the-pull-request) with a clear title and description.

**Tips**:
- For ambitious tasks, open a Pull Request as soon as possible with the `[WIP]` prefix in the title, in order to get feedback and help from the community.
- [Allow lime-elements maintainers to make changes to your Pull Request branch](https://help.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork). This way, we can rebase it and make some minor changes if necessary. All changes we make will be done in new commits and we'll ask for your approval before merging them.