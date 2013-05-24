PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py
BETACONF=$(BASEDIR)/betaconf.py

FTP_HOST=localhost
FTP_USER=anonymous
FTP_TARGET_DIR=/

SSH_HOST=achew22.com
SSH_PORT=22
SSH_USER=achew22
SSH_TARGET_DIR=/var/www/andrewzallen.com
SSH_BETA_TARGET_DIR=/var/www/beta.andrewzallen.com

DROPBOX_DIR=~/Dropbox/Public/

# Remove all files that are .less or .temp (or their gziped counterparts)
PUBLISH_IGNORE_THEME_EXTENSIONS=less less.gz tmp tmp.gz
PUBLISH_IGNORE_THEME_FOLDERS=css/bootstrap

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make publish                     generate using production settings '
	@echo '   make serve                       serve site at http://localhost:8000'
	@echo '   make devserver                   start/restart develop_server.sh    '
	@echo '   ssh_upload                       upload the web site via SSH        '
	@echo '   rsync_upload                     upload the web site via rsync+ssh  '
	@echo '   dropbox_upload                   upload the web site via Dropbox    '
	@echo '   ftp_upload                       upload the web site via FTP        '
	@echo '   github                           upload the web site via gh-pages   '
	@echo '                                                                       '


html: clean $(OUTPUTDIR)/index.html
	@echo 'Done'

$(OUTPUTDIR)/%.html:
	$(PELICAN) --debug $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	find $(OUTPUTDIR) -mindepth 1 -delete

regenerate: clean
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
	cd $(OUTPUTDIR) && python -m SimpleHTTPServer

run: devserver-stop devserver
stop: devserver-stop

devserver:
	$(BASEDIR)/develop_server.sh restart

devserver-stop:
	$(BASEDIR)/develop_server.sh stop

publish:
	$(PELICAN) -D $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
	# Now clean up assets that are temporary in the theme
	for EXT in $(PUBLISH_IGNORE_THEME_EXTENSIONS) ; do \
	find $(OUTPUTDIR)/theme -name "*.$$EXT" -mindepth 1 -delete ; done

	for FOLDER in $(PUBLISH_IGNORE_THEME_FOLDERS) ; do \
	rm -rf $(OUTPUTDIR)/theme/$$FOLDER ; done

scp_upload: publish
	rm $(OUTPUTDIR)/htpasswd
	scp -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

beta:
	make -e PUBLISHCONF=$(BETACONF) publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvz --delete $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_BETA_TARGET_DIR)

ssh_upload: publish
	rm $(OUTPUTDIR)/htpasswd
	rsync -e "ssh -p $(SSH_PORT)" -P -rvz --delete $(OUTPUTDIR) $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

dropbox_upload: publish
	cp -r $(OUTPUTDIR)/* $(DROPBOX_DIR)

ftp_upload: publish
	lftp ftp://$(FTP_USER)@$(FTP_HOST) -e "mirror -R $(OUTPUTDIR) $(FTP_TARGET_DIR) ; quit"

github: publish
	ghp-import $(OUTPUTDIR)
	git push origin gh-pages

.PHONY: html help clean regenerate serve devserver publish ssh_upload beta rsync_upload dropbox_upload ftp_upload github
