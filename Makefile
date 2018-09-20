
dev:
	vuepress dev

site:
	vuepress build
	rsync -azv .vuepress/dist/* ${USER}@learnartthehardway.com:/var/www/learnartthehardway.com/
