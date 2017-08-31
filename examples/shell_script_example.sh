#!/bin/bash

source $SKMD_PATH/skm-data.sh

function make_new_skmd_configuration () {
    dir=$1
    error_if_exists=$2
    skmd new -d $dir --error-if-exists $error_if_exists
    skmd upgrade -n machine_identity -name "ABC machine" \
                                     -role "ABC role" \
                                     -system ubuntu \
                                     -ial_id 0 \
                                     -ial_rayss ial_kepler \
                                     -ial_rayss_adress ial_rayss_kepler
    skmd upgrade -n machine_caracteristics -type virtual \
                                           -hardware \
                                           -location
    skmd upgrade -n machine_dirs -home_path /home/ubuntu \
                                 -working_path /home/ubuntu/shit
    skmd upgrade -e machine_dirs -working_path /home/ubuntu/work
    skmd upgrade -n babtu -babtu_is_here False \
                          -make_packages False \
                          -auto_upgrade False
    skmd upgrade -n babtu.packages -ialcloud \
                                   -pip \
                                   -apt
    skmd upgrade -n machine_storage -sgbd mysql \
                                    -sgbd_server_local False \
                                    -skmvs_local True
    skmd upgrade -n mysql.logs -host localhost \
                               -port 22 \
                               -user root \
                               -password uehMLMRw
    skmd upgrade -n mysql.config -raise_on_warnings True \
                                 -use_pure True
}

make_new_skmd_configuration $1 $2
