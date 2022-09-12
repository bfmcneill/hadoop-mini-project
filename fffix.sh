
# to clean up issues with *.py file new lines between unix / windows run this script
# https://stackoverflow.com/a/36885829

for file in *.py ; do
    vi +':w ++ff=unix' +':q' "${file}"
done

for file in *.sh ; do
    vi +':w ++ff=unix' +':q' "${file}"
done
