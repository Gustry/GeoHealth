#!/bin/bash

SAFE_PYFILES=`find src -name "**.py**" | grep -v "pyc$" | grep -v test`
UI_FILES=`find src -name "**.ui**"`

PRO_FILE=geohealth.pro

echo "SOURCES = \\" > ${PRO_FILE}

# First add the SAFE files to the pro file
for FILE in ${SAFE_PYFILES}
do
  echo "    ${FILE} \\"  >> ${PRO_FILE}
done

echo "
FORMS = \\" >> ${PRO_FILE}

LAST_FILE=""
for FILE in ${UI_FILES}
do
        if [ ! -z ${LAST_FILE} ]
        then
                echo "    ${LAST_FILE} \\" >> ${PRO_FILE}
        fi
        LAST_FILE=${FILE}
done
if [ ! -z ${LAST_FILE} ]
then
        echo "    ${LAST_FILE}" >> ${PRO_FILE}
fi

# Finally define which languages we are translating for

echo "
TRANSLATIONS = src/i18n/geohealth_fr.ts \\
               src/i18n/geohealth_th.ts"  >> ${PRO_FILE}
