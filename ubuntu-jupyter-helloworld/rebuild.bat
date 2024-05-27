vagrant destroy -f

echo "build start"

vagrant up
@REM vagrant plugin install vagrant-share

echo "build done"

vagrant ssh
