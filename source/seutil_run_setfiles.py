
from source.lib import Data, Hlink

def seutil_run_setfiles():
    return\
    Data(title = 'Раскрытие макроса SELinux - seutil_run_setfiles',
        schema = {'m000':
                   [
                    {'m01':
                         ['m10',
                          {'m11':
                               ['m20',
                                {'m21':  # files_search_usr
                                     ['m30',
                                      'm31']
                                 },
                                {'m22':  # corecmd_search_bin
                                     ['m32',
                                      {'m33':  # read_lnk_files_pattern()
                                           ['m40',
                                            'm41']
                                       },
                                      {'m34':  # files_search_usr
                                           ['m42',
                                            'm43']
                                       }]
                                 },
                                {'m23':
                                     [{'m35':
                                           [{'m44': ['m50', 'm51', 'm52']},
                                            'm45']},
                                      'm36',
                                      'm37',
                                      'm38']
                                 }]
                           },
                          'm12']},
                    'm02',
                    'm03',
                    'm00',]},
    voc = {
        'm000': ["userdom_security_admin_template", "`userdom_security_admin_template", 0],
        'm00': ["прочие макросы", "прочие макросы", 0],
        'm01': ["seutil_run_setfiles(domain , role)", "seutil_run_setfiles($1, $2)", 0],
        'm02': ["прочие инструкции", "прочие инструкции", 0],
        'm03': ["seutil_run_semanage(domain , role)", "см. соответствующую схему", 0],
        'm10': ["gen_require", "gen_require(`type setfiles_t;')", 0],
        'm11': ["seutil_domtrans_setfiles()", "seutil_domtrans_setfiles(1)", 0],
        'm12': ["role 2 types setfiles_t", "role $2 types setfiles_t;", 0],
        'm20': ["gen_require", "gen_require(`type setfiles_t, setfiles_exec_t;')", 0],
        'm21': ["files_search_usr()", "files_search_usr($1)", 0],
        'm22': ["corecmd_search_bin()", "corecmd_search_bin($1)", 0],
        'm23': ["domtrans_pattern()", "domtrans_pattern($1, setfiles_exec_t, setfiles_t)<br>/usr/share/selinux/devel/include/support/misc_patterns.spt", 0],
        'm30': ["gen_require", "gen_require(`type usr_t;')", 1],
        'm31': ["allow 1 usr_t:dir search_dir_perms;", "allow $1 usr_t:dir search_dir_perms;", 0],
        'm32': ["gen_require", "gen_require(`type bin_t;')", 0],
        'm33': ["read_lnk_files_pattern()", "read_lnk_files_pattern($1, bin_t, bin_t)<br>/usr/share/selinux/devel/include/support/file_patterns.spt", 0],
        'm34': ["files_search_usr()", "files_search_usr($1)", 0],
        'm35': ["domain_auto_transition_pattern()", "domain_auto_transition_pattern($1, $2, $3)<br>/usr/share/selinux/devel/include/support/misc_patterns.spt", 0],
        'm36': ["allow 3 1:fd use", "allow $3 $1:fd use;", 0],
        'm37': ["allow 3 1:fifo_file rw_inherited_fifo_file_perms",
                "allow $3 $1:fifo_file rw_inherited_fifo_file_perms;", 0],
        'm38': ["allow 3 1:process sigchld", "allow $3 $1:process sigchld;", 0],
        'm40': ["allow 1 2:dir search_dir_perms", "allow $1 $2:dir search_dir_perms;", 0],
        'm41': ["allow 1 3:lnk_file read_lnk_file_perms", "allow $1 $3:lnk_file read_lnk_file_perms;", 0],
        'm42': ["gen_require", "gen_require(`type usr_t;')", 0],
        'm43': ["allow 1 usr_t:dir search_dir_perms;", "allow $1 usr_t:dir search_dir_perms;", 0],
        'm44': ["domain_transition_pattern()", "domain_transition_pattern($1,$2,$3)<br>/usr/share/selinux/devel/include/support/misc_patterns.spt", 0],
        'm45': ["type_transition 1 2:process 3", "type_transition $1 $2:process $3;", 0],
        'm50': ["allow 1 2:file mmap_exec_file_perms", "allow $1 $2:file mmap_exec_file_perms;", 0],
        'm51': ["allow 1 3:process transition", "allow $1 $3:process transition;", 0],
        'm52': ["dontaudit process", "dontaudit $ 1 $ 3:process { noatsecure siginh rlimitinh };", 0],
    },
    link={
        'm000': Hlink('userdomain.if', "https://github.com/fedora-selinux/selinux-policy/blob/rawhide/policy/modules/system/userdomain.if#L6602"),
        #'m00': Hlink('', ''),
        'm01': Hlink('selinuxutil.if', 'https://github.com/fedora-selinux/selinux-policy/blob/rawhide/policy/modules/system/selinuxutil.if#L612'),
        #'m02': Hlink('', ''),
        'm10': Hlink('', ''),
        'm11': Hlink('selinuxutil.if', 'https://github.com/fedora-selinux/selinux-policy/blob/rawhide/policy/modules/system/selinuxutil.if#L584'),
        #'m12': Hlink('', ''),
        #'m20': Hlink('', ''),
        'm21': Hlink('files.if', 'https://github.com/fedora-selinux/selinux-policy/blob/rawhide/policy/modules/kernel/files.if#L6343'),
        'm22': Hlink('corecommands.if', 'https://github.com/fedora-selinux/selinux-policy/blob/rawhide/policy/modules/kernel/corecommands.if#L138'),
        'm23': Hlink('misc_patterns.spt', 'https://github.com/fedora-selinux/selinux-policy/blob/rawhide/policy/support/misc_patterns.spt#L33'),
        #'m30': Hlink('', ''),
        #'m31': Hlink('', ''),
        #'m32': Hlink('', ''),
        'm33': Hlink('file_patterns.spt', 'https://github.com/fedora-selinux/selinux-policy/blob/rawhide/policy/support/file_patterns.spt#L197'),
        'm34': Hlink('files.if', 'https://github.com/fedora-selinux/selinux-policy/blob/rawhide/policy/modules/kernel/files.if#L6343'),
        'm35': Hlink('misc_patterns.spt', 'https://github.com/fedora-selinux/selinux-policy/blob/rawhide/policy/support/misc_patterns.spt#L25'),
        #'m36': Hlink('', ''),
        #'m37': Hlink('', ''),
        #'m38': Hlink('', ''),
        #'m40': Hlink('', ''),
        #'m41': Hlink('', ''),
        #'m42': Hlink('', ''),
        #'m43': Hlink('', ''),
        'm44': Hlink('misc_patterns.spt', 'https://github.com/fedora-selinux/selinux-policy/blob/rawhide/policy/support/misc_patterns.spt#L4'),
        #'m45': Hlink('', ''),
        #'m50': Hlink('', ''),
        #'m51': Hlink('', ''),
        #'m52': Hlink('', ''),
    }
         )
