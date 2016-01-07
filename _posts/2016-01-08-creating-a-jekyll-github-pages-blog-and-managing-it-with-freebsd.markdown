---
layout: post
title:  "Creating A Jekyll GitHub Pages Blog and Managing it With FreeBSD"
date:   2016-01-08 03:07:15 +0900
categories: jekyll github freebsd
---
First, create a new GitHub repository named my_username.github.io, where my_username is your GitHub username.

Next, install Jekyll, create a new blog and push it to github.
```sh
{% highlight sh %}
# install jekyll
su
portmaster devel/ruby-gems
gem install jekyll
exit

# create a new blog
mkdir my_blog
cd my_blog
jekyll new my_username.github.io
cd my_username.github.io

# add ssh key to session using the sh shell
# assumes you are set up to use ssh
sh
eval "$(ssh-agent -s)”
ssh-add ~/.ssh/id_rss

# add project to git and push to github
git init
git add .
git commit -m “Initial commit.”
git remote add origin git@github.com:my_username/my_username.github.io.git
git remote -v
git push origin master

# configure blog
vim _config.yml

# save welcome post in drafts
mkdir _drafts
cp _posts/YYYY-MM-DD-welcome-to-jekyll.markdown _drafts/

# create post
vim _posts/YYYY-MM-DD-name-of-post.markdown

# build local site
jekyll build --incremental --drafts

# sync changes
git add .
git commit -m “Change message."
git push
{% endhighlight %}


## References:
- [GitHub Pages Setup Instructions](https://pages.github.com)
- [GitHub Markdown Basics](https://help.github.com/articles/markdown-basics/)
- [GitHub Generating SSH Keys](https://help.github.com/articles/generating-ssh-keys/)
- [GitHub Add Existing Project](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/)
- [Jekyll Quick-Start Guide](http://jekyllrb.com/docs/quickstart/)
- [Jekyll Configuration](http://jekyllrb.com/docs/configuration/)
- [Jekyll Writing posts](http://jekyllrb.com/docs/posts/)
- [Jekyll Working with drafts](http://jekyllrb.com/docs/drafts/)
- [Jekyll bug: Tag was never closed](http://blog.slaks.net/2013-08-09/jekyll-tag-was-never-closed/)
- [FreeBSD Handbook Using the Ports Collection](https://www.freebsd.org/doc/handbook/ports-using.html)

