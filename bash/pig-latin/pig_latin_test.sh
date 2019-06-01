#!/usr/bin/env bash

# "ay" is added to words that start with vowels

@test word_beginning_with_a {
    run bash pig_latin.sh apple
    [[ $status -eq 0 ]]
    [[ $output == "appleay" ]]
}

@test word_beginning_with_e {
    run bash pig_latin.sh ear
    [[ $status -eq 0 ]]
    [[ $output == "earay" ]]
}

@test word_beginning_with_i {
    run bash pig_latin.sh igloo
    [[ $status -eq 0 ]]
    [[ $output == "iglooay" ]]
}

@test word_beginning_with_o {
    run bash pig_latin.sh object
    [[ $status -eq 0 ]]
    [[ $output == "objectay" ]]
}

@test word_beginning_with_u {
    run bash pig_latin.sh under
    [[ $status -eq 0 ]]
    [[ $output == "underay" ]]
}

@test word_beginning_with_equ {
    run bash pig_latin.sh equal
    [[ $status -eq 0 ]]
    [[ $output == "equalay" ]]
}

# first letter and ay are moved to the end of words that start with consonants

@test word_beginning_with_p {
    run bash pig_latin.sh pig
    [[ $status -eq 0 ]]
    [[ $output == "igpay" ]]
}

@test word_beginning_with_k {
    run bash pig_latin.sh koala
    [[ $status -eq 0 ]]
    [[ $output == "oalakay" ]]
}

@test word_beginning_with_x {
    run bash pig_latin.sh xenon
    [[ $status -eq 0 ]]
    [[ $output == "enonxay" ]]
}

@test word_beginning_with_q_no_u {
    run bash pig_latin.sh qat
    [[ $status -eq 0 ]]
    [[ $output == "atqay" ]]
}

# some letter clusters are treated like a single consonant

@test word_beginning_with_ch {
    run bash pig_latin.sh chair
    [[ $status -eq 0 ]]
    [[ $output == "airchay" ]]
}

@test word_beginning_with_squ {
    run bash pig_latin.sh square
    [[ $status -eq 0 ]]
    [[ $output == "aresquay" ]]
}

@test word_beginning_with_th {
    run bash pig_latin.sh therapy
    [[ $status -eq 0 ]]
    [[ $output == "erapythay" ]]
}

@test word_beginning_with_thr {
    run bash pig_latin.sh thrush
    [[ $status -eq 0 ]]
    [[ $output == "ushthray" ]]
}

@test word_beginning_with_sch {
    run bash pig_latin.sh school
    [[ $status -eq 0 ]]
    [[ $output == "oolschay" ]]
}

# some letter clusters are treated like a single vowel

@test word_beginning_with_yt {
    run bash pig_latin.sh yttria
    [[ $status -eq 0 ]]
    [[ $output == "yttriaay" ]]
}

@test word_beginning_with_xr {
    run bash pig_latin.sh xray
    [[ $status -eq 0 ]]
    [[ $output == "xrayay" ]]
}

# position of y in a word determines if it is a consonant or a vowel

@test word_beginning_with_y {
    run bash pig_latin.sh yellow
    [[ $status -eq 0 ]]
    [[ $output == "ellowyay" ]]
}

@test word_rhythm {
    run bash pig_latin.sh rhythm
    [[ $status -eq 0 ]]
    [[ $output == "ythmrhay" ]]
}

@test word_my {
    run bash pig_latin.sh my
    [[ $status -eq 0 ]]
    [[ $output == "ymay" ]]
}

# phrases are translated
@test a_whole_phrase {
    run bash pig_latin.sh quick fast run
    [[ $status -eq 0 ]]
    [[ $output == "ickquay astfay unray" ]]
}
