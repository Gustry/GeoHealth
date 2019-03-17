#!/bin/bash
LOCALES=$*

python_safe=`find src/ -regex ".*\(ui\|py\)$" -type f`

# update .ts
echo "Please provide translations by editing the translation files below:"
for LOCALE in ${LOCALES}
do
echo "i18n/geohealth_"${LOCALE}".ts"
# Note we don't use pylupdate with qt .pro file approach as it is flakey
# about what is made available.
set -x
pylupdate4 -noobsolete ${python_safe} -ts src/i18n/geohealth_${LOCALE}.ts
done

