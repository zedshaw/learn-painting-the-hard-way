
dev:
	vuepress dev

site:
	vuepress build
	rsync --delete -azv .vuepress/dist/* ${USER}@learnartthehardway.com:/var/www/learnartthehardway.com/
