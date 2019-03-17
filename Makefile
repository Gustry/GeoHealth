
# Run pep8 style checking
#http://pypi.python.org/pypi/pep8
pep8:
	@echo
	@echo "-----------"
	@echo "PEP8 issues"
	@echo "-----------"
	@pep8 --version
	@pep8 --repeat --ignore=E203,E121,E122,E123,E124,E125,E126,E127,E128,E402 --exclude resources_rc.py,geohealth/ui/  . || true

# LOCALES = space delimited list of iso codes to generate po files for
# Please dont remove en here
LOCALES = en fr th pt_BR

#Qt .ts file updates - run to register new strings for translation in safe_qgis
update-translation-strings:
        #update application strings
	@echo "Checking current translation."
	@scripts/update-strings.sh $(LOCALES)

#Qt .qm file updates - run to create binary representation of translated strings for translation in safe_qgis
compile-translation-strings:
	@#Compile qt messages binary
	@scripts/create_pro_file.sh
	@lrelease-qt4 geohealth.pro
	@rm geohealth.pro

test-translations:
	@echo
	@echo "----------------------------------------------------------------"
	@echo "Missing translations - for more info run: make translation-stats"
	@echo "----------------------------------------------------------------"
	@python scripts/missing_translations.py `pwd` fr
	@python scripts/missing_translations.py `pwd` th


translation-stats:
	@echo
	@echo "----------------------"
	@echo "Translation statistics - for more info see http://inasafe.org/developer-docs/i18n.html"
	@echo "----------------------"
	@echo
	@echo "Qt translations (*.ts):"
	@echo "----------------------------"
	@scripts/string-stats.sh

docker-update-translation-strings:
	@echo "Update translation using docker"
	@docker run -t -i -v $(DIR):/home kartoza/qt-translation make update-translation-strings

docker-compile-translation-strings:
	@echo "Update translation using docker"
	@docker run -t -i -v $(DIR):/home kartoza/qt-translation make compile-translation-strings

docker-test-translation:
	@echo "Update translation using docker"
	@docker run -t -i -v $(DIR):/home kartoza/qt-translation make test-translations
