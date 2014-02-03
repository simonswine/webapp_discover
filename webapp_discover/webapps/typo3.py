__author__ = 'christian'

import os
import re

from webapp_discover.php_webapp import PhpWebApp

RE_VERSION_OLD = re.compile("""\$TYPO_VERSION\s+=\s+['"](\d+(\.\d+)+)['"]""")
RE_VERSION = re.compile("""["']TYPO3_version["']\s*,\s*['"](\d+(\.\d+)+)['"]""")


class Typo3WebApp(PhpWebApp):

    webapp_name = "Typo3"
    webapp_files = [
        './ChangeLog',
        './clear.gif',
        './fileadmin/_temp_/.htaccess',
        './fileadmin/_temp_/index.html',
        './GPL.txt',
        './_.htaccess',
        './index.php',
        './INSTALL.txt',
        './LICENSE.txt',
        './NEWS.txt',
        './README.txt',
        './RELEASE_NOTES.txt',
        './t3lib/cache/backend/class.t3lib_cache_backend_abstractbackend.php',
        './t3lib/cache/backend/class.t3lib_cache_backend_apcbackend.php',
        './t3lib/cache/backend/class.t3lib_cache_backend_dbbackend.php',
        './t3lib/cache/backend/class.t3lib_cache_backend_filebackend.php',
        './t3lib/cache/backend/class.t3lib_cache_backend_memcachedbackend.php',
        './t3lib/cache/backend/class.t3lib_cache_backend_nullbackend.php',
        './t3lib/cache/backend/class.t3lib_cache_backend_pdobackend.php',
        './t3lib/cache/backend/class.t3lib_cache_backend_transientmemorybackend.php',
        './t3lib/cache/backend/interfaces/interface.t3lib_cache_backend_backend.php',
        './t3lib/cache/backend/interfaces/interface.t3lib_cache_backend_phpcapablebackend.php',
        './t3lib/cache/class.t3lib_cache_exception.php',
        './t3lib/cache/class.t3lib_cache_factory.php',
        './t3lib/cache/class.t3lib_cache_manager.php',
        './t3lib/cache/exception/class.t3lib_cache_exception_classalreadyloaded.php',
        './t3lib/cache/exception/class.t3lib_cache_exception_duplicateidentifier.php',
        './t3lib/cache/exception/class.t3lib_cache_exception_invalidbackend.php',
        './t3lib/cache/exception/class.t3lib_cache_exception_invalidcache.php',
        './t3lib/cache/exception/class.t3lib_cache_exception_invaliddata.php',
        './t3lib/cache/exception/class.t3lib_cache_exception_nosuchcache.php',
        './t3lib/cache/frontend/class.t3lib_cache_frontend_abstractfrontend.php',
        './t3lib/cache/frontend/class.t3lib_cache_frontend_phpfrontend.php',
        './t3lib/cache/frontend/class.t3lib_cache_frontend_stringfrontend.php',
        './t3lib/cache/frontend/class.t3lib_cache_frontend_variablefrontend.php',
        './t3lib/cache/frontend/interfaces/interface.t3lib_cache_frontend_frontend.php',
        './t3lib/class.t3lib_admin.php',
        './t3lib/class.t3lib_ajax.php',
        './t3lib/class.t3lib_arraybrowser.php',
        './t3lib/class.t3lib_autoloader.php',
        './t3lib/class.t3lib_basicfilefunc.php',
        './t3lib/class.t3lib_befunc.php',
        './t3lib/class.t3lib_beuserauth.php',
        './t3lib/class.t3lib_browsetree.php',
        './t3lib/class.t3lib_cache.php',
        './t3lib/class.t3lib_clipboard.php',
        './t3lib/class.t3lib_cli.php',
        './t3lib/class.t3lib_compressor.php',
        './t3lib/class.t3lib_cs.php',
        './t3lib/class.t3lib_db.php',
        './t3lib/class.t3lib_diff.php',
        './t3lib/class.t3lib_div.php',
        './t3lib/class.t3lib_exception.php',
        './t3lib/class.t3lib_exec.php',
        './t3lib/class.t3lib_extfilefunc.php',
        './t3lib/class.t3lib_extmgm.php',
        './t3lib/class.t3lib_extobjbase.php',
        './t3lib/class.t3lib_flashmessage.php',
        './t3lib/class.t3lib_flashmessagequeue.php',
        './t3lib/class.t3lib_flexformtools.php',
        './t3lib/class.t3lib_foldertree.php',
        './t3lib/class.t3lib_formmail.php',
        './t3lib/class.t3lib_frontendedit.php',
        './t3lib/class.t3lib_fullsearch.php',
        './t3lib/class.t3lib_iconworks.php',
        './t3lib/class.t3lib_install.php',
        './t3lib/class.t3lib_loaddbgroup.php',
        './t3lib/class.t3lib_loadmodules.php',
        './t3lib/class.t3lib_lock.php',
        './t3lib/class.t3lib_modsettings.php',
        './t3lib/class.t3lib_page.php',
        './t3lib/class.t3lib_pagerenderer.php',
        './t3lib/class.t3lib_pagetree.php',
        './t3lib/class.t3lib_parsehtml.php',
        './t3lib/class.t3lib_parsehtml_proc.php',
        './t3lib/class.t3lib_pdohelper.php',
        './t3lib/class.t3lib_positionmap.php',
        './t3lib/class.t3lib_querygenerator.php',
        './t3lib/class.t3lib_readmail.php',
        './t3lib/class.t3lib_recordlist.php',
        './t3lib/class.t3lib_refindex.php',
        './t3lib/class.t3lib_registry.php',
        './t3lib/class.t3lib_rteapi.php',
        './t3lib/class.t3lib_scbase.php',
        './t3lib/class.t3lib_softrefproc.php',
        './t3lib/class.t3lib_spritemanager.php',
        './t3lib/class.t3lib_sqlparser.php',
        './t3lib/class.t3lib_stdgraphic.php',
        './t3lib/class.t3lib_svbase.php',
        './t3lib/class.t3lib_syntaxhl.php',
        './t3lib/class.t3lib_tceforms_fe.php',
        './t3lib/class.t3lib_tceforms_inline.php',
        './t3lib/class.t3lib_tceforms.php',
        './t3lib/class.t3lib_tcemain.php',
        './t3lib/class.t3lib_timetracknull.php',
        './t3lib/class.t3lib_timetrack.php',
        './t3lib/class.t3lib_transferdata.php',
        './t3lib/class.t3lib_transl8tools.php',
        './t3lib/class.t3lib_treeview.php',
        './t3lib/class.t3lib_tsfebeuserauth.php',
        './t3lib/class.t3lib_tsparser_ext.php',
        './t3lib/class.t3lib_tsparser.php',
        './t3lib/class.t3lib_tsparser_tsconfig.php',
        './t3lib/class.t3lib_tsstyleconfig.php',
        './t3lib/class.t3lib_tstemplate.php',
        './t3lib/class.t3lib_userauthgroup.php',
        './t3lib/class.t3lib_userauth.php',
        './t3lib/class.t3lib_xml.php',
        './t3lib/csconvtbl/ascii.tbl',
        './t3lib/csconvtbl/big5.tbl',
        './t3lib/csconvtbl/euc-kr.tbl',
        './t3lib/csconvtbl/gb2312.tbl',
        './t3lib/csconvtbl/iso-8859-10.tbl',
        './t3lib/csconvtbl/iso-8859-11.tbl',
        './t3lib/csconvtbl/iso-8859-13.tbl',
        './t3lib/csconvtbl/iso-8859-14.tbl',
        './t3lib/csconvtbl/iso-8859-15.tbl',
        './t3lib/csconvtbl/iso-8859-16.tbl',
        './t3lib/csconvtbl/iso-8859-1.tbl',
        './t3lib/csconvtbl/iso-8859-2.tbl',
        './t3lib/csconvtbl/iso-8859-3.tbl',
        './t3lib/csconvtbl/iso-8859-4.tbl',
        './t3lib/csconvtbl/iso-8859-5.tbl',
        './t3lib/csconvtbl/iso-8859-6.tbl',
        './t3lib/csconvtbl/iso-8859-7.tbl',
        './t3lib/csconvtbl/iso-8859-8.tbl',
        './t3lib/csconvtbl/iso-8859-9.tbl',
        './t3lib/csconvtbl/koi8-r.tbl',
        './t3lib/csconvtbl/readme.txt',
        './t3lib/csconvtbl/shift_jis.tbl',
        './t3lib/csconvtbl/windows-1250.tbl',
        './t3lib/csconvtbl/windows-1251.tbl',
        './t3lib/csconvtbl/windows-1252.tbl',
        './t3lib/csconvtbl/windows-1253.tbl',
        './t3lib/csconvtbl/windows-1254.tbl',
        './t3lib/csconvtbl/windows-1255.tbl',
        './t3lib/csconvtbl/windows-1256.tbl',
        './t3lib/csconvtbl/windows-1257.tbl',
        './t3lib/csconvtbl/windows-1258.tbl',
        './t3lib/csconvtbl/windows-874.tbl',
        './t3lib/error/class.t3lib_error_abstractexceptionhandler.php',
        './t3lib/error/class.t3lib_error_debugexceptionhandler.php',
        './t3lib/error/class.t3lib_error_errorhandler.php',
        './t3lib/error/class.t3lib_error_exception.php',
        './t3lib/error/class.t3lib_error_productionexceptionhandler.php',
        './t3lib/error/interface.t3lib_error_errorhandlerinterface.php',
        './t3lib/error/interface.t3lib_error_exceptionhandlerinterface.php',
        './t3lib/extjs/class.t3lib_extjs_extdirectapi.php',
        './t3lib/extjs/class.t3lib_extjs_extdirectrouter.php',
        './t3lib/GPL.txt',
        './t3lib/index.html',
        './t3lib/interfaces/interface.t3lib_browselinkshook.php',
        './t3lib/interfaces/interface.t3lib_localrecordlistgettablehook.php',
        './t3lib/interfaces/interface.t3lib_pageselect_getpagehook.php',
        './t3lib/interfaces/interface.t3lib_pageselect_getpageoverlayhook.php',
        './t3lib/interfaces/interface.t3lib_pageselect_getrecordoverlayhook.php',
        './t3lib/interfaces/interface.t3lib_singleton.php',
        './t3lib/interfaces/interface.t3lib_spritemanager_spriteicongenerator.php',
        './t3lib/interfaces/interface.t3lib_tceformsinlinehook.php',
        './t3lib/interfaces/interface.t3lib_tcemain_checkmodifyaccesslisthook.php',
        './t3lib/js/adminpanel.js',
        './t3lib/js/extjs/tceforms.js',
        './t3lib/js/extjs/ux/ext.resizable.js',
        './t3lib/js/extjs/ux/ext.ux.tabclosemenu.js',
        './t3lib/js/extjs/ux/flashmessages.js',
        './t3lib/js/extjs/ux/resize.css',
        './t3lib/js/extjs/ux/resize.gif',
        './t3lib/jsfunc.evalfield.js',
        './t3lib/jsfunc.inline.js',
        './t3lib/jsfunc.menu.js',
        './t3lib/jsfunc.updateform.js',
        './t3lib/jsfunc.validateform.js',
        './t3lib/js/jsfunc.tceforms_suggest.js',
        './t3lib/matchcondition/class.t3lib_matchcondition_abstract.php',
        './t3lib/matchcondition/class.t3lib_matchcondition_backend.php',
        './t3lib/matchcondition/class.t3lib_matchcondition_frontend.php',
        './t3lib/README.txt',
        './t3lib/spritemanager/class.t3lib_spritemanager_simplehandler.php',
        './t3lib/tceforms/class.t3lib_tceforms_suggest_defaultreceiver.php',
        './t3lib/tceforms/class.t3lib_tceforms_suggest.php',
        './t3lib/thumbs.php',
        './t3lib/unidata/SpecialCasing.txt',
        './t3lib/unidata/Translit.txt',
        './t3lib/unidata/UnicodeData.txt',
        './t3lib/utility/class.t3lib_utility_client.php',
        './t3lib/utility/class.t3lib_utility_http.php',
        './t3lib/utility/class.t3lib_utility_mail.php',
        './typo3/alt_clickmenu.php',
        './typo3/alt_db_navframe.php',
        './typo3/alt_doc_nodoc.php',
        './typo3/alt_doc.php',
        './typo3/alt_file_navframe.php',
        './typo3/alt_shortcut.php',
        './typo3/browse_links.php',
        './typo3/browser.php',
        './typo3/class.db_list_extra.inc',
        './typo3/class.db_list.inc',
        './typo3/class.file_list.inc',
        './typo3/class.show_rechis.inc',
        './typo3/clear.gif',
        './typo3/close.html',
        './typo3conf/extTables.php',
        './typo3conf/index.html',
        './typo3/db_new.php',
        './typo3/dummy.php',
        './typo3/ext/README.txt',
        './typo3/file_edit.php',
        './typo3/file_newfolder.php',
        './typo3/file_rename.php',
        './typo3/file_upload.php',
        './typo3/GPL.txt',
        './typo3/init.php',
        './typo3/install/_.htaccess',
        './typo3/install/index.php',
        './typo3/install/README.txt',
        './typo3/LICENSE.txt',
        './typo3/listframe_loader.php',
        './typo3/login_frameset.php',
        './typo3/logout.php',
        './typo3/md5.js',
        './typo3/mod/file/conf.php',
        './typo3/mod/file/file.gif',
        './typo3/mod/help/clear.gif',
        './typo3/mod/help/conf.php',
        './typo3/mod/help/help.gif',
        './typo3/mod/README.txt',
        './typo3/mod/tools/clear.gif',
        './typo3/mod/tools/conf.php',
        './typo3/mod/tools/note.txt',
        './typo3/mod/tools/tool.gif',
        './typo3/mod/user/clear.gif',
        './typo3/mod/user/conf.php',
        './typo3/mod/user/user.gif',
        './typo3/mod/web/clear.gif',
        './typo3/mod/web/conf.php',
        './typo3/mod/web/website.gif',
        './typo3/move_el.php',
        './typo3/README.txt',
        './typo3/show_item.php',
        './typo3/show_rechis.php',
        './typo3/sysext/aboutmodules/ext_emconf.php',
        './typo3/sysext/aboutmodules/ext_icon.gif',
        './typo3/sysext/aboutmodules/ext_tables.php',
        './typo3/sysext/cms/cshimages/localizationoverview1.png',
        './typo3/sysext/cms/cshimages/localizationoverview.png',
        './typo3/sysext/cms/cshimages/pagemodule_10.png',
        './typo3/sysext/cms/cshimages/pagemodule_11.png',
        './typo3/sysext/cms/cshimages/pagemodule_12.png',
        './typo3/sysext/cms/cshimages/pagemodule_13.png',
        './typo3/sysext/cms/cshimages/pagemodule_14.png',
        './typo3/sysext/cms/cshimages/pagemodule_15.png',
        './typo3/sysext/cms/cshimages/pagemodule_1.png',
        './typo3/sysext/cms/cshimages/pagemodule_2.png',
        './typo3/sysext/cms/cshimages/pagemodule_4.png',
        './typo3/sysext/cms/cshimages/pagemodule_5.png',
        './typo3/sysext/cms/cshimages/pagemodule_6.png',
        './typo3/sysext/cms/cshimages/pagemodule_7.png',
        './typo3/sysext/cms/cshimages/pagemodule_9.png',
        './typo3/sysext/cms/cshimages/pagetree_overview_1.png',
        './typo3/sysext/cms/cshimages/pagetree_overview_2.png',
        './typo3/sysext/cms/cshimages/pagetree_overview_3.png',
        './typo3/sysext/cms/cshimages/pagetree_overview_4.png',
        './typo3/sysext/cms/cshimages/pagetree_overview_5.png',
        './typo3/sysext/cms/cshimages/pagetree_overview_6.png',
        './typo3/sysext/cms/cshimages/pagetree_overview_7.png',
        './typo3/sysext/cms/cshimages/pagetree_overview_8.png',
        './typo3/sysext/cms/cshimages/pagetree_overview_9.png',
        './typo3/sysext/cms/ext_emconf.php',
        './typo3/sysext/cms/ext_icon.gif',
        './typo3/sysext/cms/ext_localconf.php',
        './typo3/sysext/cms/ext_tables.php',
        './typo3/sysext/cms/ext_tables.sql',
        './typo3/sysext/cms/layout/class.tx_cms_layout.php',
        './typo3/sysext/cms/layout/clear.gif',
        './typo3/sysext/cms/layout/conf.php',
        './typo3/sysext/cms/layout/db_layout.php',
        './typo3/sysext/cms/layout/db_new_content_el.php',
        './typo3/sysext/cms/layout/layout.gif',
        './typo3/sysext/cms/tslib/class.tslib_content.php',
        './typo3/sysext/cms/tslib/class.tslib_fe.php',
        './typo3/sysext/cms/tslib/class.tslib_feuserauth.php',
        './typo3/sysext/cms/tslib/class.tslib_gifbuilder.php',
        './typo3/sysext/cms/tslib/class.tslib_menu.php',
        './typo3/sysext/cms/tslib/class.tslib_pagegen.php',
        './typo3/sysext/cms/tslib/class.tslib_pibase.php',
        './typo3/sysext/cms/tslib/class.tslib_search.php',
        './typo3/sysext/cms/tslib/index_ts.php',
        './typo3/sysext/cms/tslib/pagegen.php',
        './typo3/sysext/cms/tslib/showpic.php',
        './typo3/sysext/cms/web_info/class.tx_cms_webinfo_lang.php',
        './typo3/sysext/cms/web_info/class.tx_cms_webinfo.php',
        './typo3/sysext/context_help/cshimages/fegroups_3.png',
        './typo3/sysext/context_help/cshimages/fegroups_4.png',
        './typo3/sysext/context_help/cshimages/feusers_1.png',
        './typo3/sysext/context_help/cshimages/feusers_2.png',
        './typo3/sysext/context_help/cshimages/hidden_page.gif',
        './typo3/sysext/context_help/cshimages/hidden_page.png',
        './typo3/sysext/context_help/cshimages/pages_1.png',
        './typo3/sysext/context_help/cshimages/pages_2.png',
        './typo3/sysext/context_help/cshimages/page_shortcut.gif',
        './typo3/sysext/context_help/cshimages/page_shortcut.png',
        './typo3/sysext/context_help/cshimages/static.png',
        './typo3/sysext/context_help/cshimages/systemplate1.png',
        './typo3/sysext/context_help/cshimages/systemplate2.png',
        './typo3/sysext/context_help/cshimages/systemplate.png',
        './typo3/sysext/context_help/cshimages/ttcontent_1.png',
        './typo3/sysext/context_help/cshimages/ttcontent_2.png',
        './typo3/sysext/context_help/cshimages/ttcontent_3.png',
        './typo3/sysext/context_help/cshimages/ttcontent_4.png',
        './typo3/sysext/context_help/cshimages/ttcontent_5.png',
        './typo3/sysext/context_help/cshimages/ttcontent_6.png',
        './typo3/sysext/context_help/cshimages/ttcontent_7.png',
        './typo3/sysext/context_help/ext_emconf.php',
        './typo3/sysext/context_help/ext_icon.gif',
        './typo3/sysext/context_help/ext_tables.php',
        './typo3/sysext/extra_page_cm_options/class.tx_extrapagecmoptions.php',
        './typo3/sysext/extra_page_cm_options/ext_emconf.php',
        './typo3/sysext/extra_page_cm_options/ext_icon.gif',
        './typo3/sysext/extra_page_cm_options/ext_tables.php',
        './typo3/sysext/func_wizards/class.tx_funcwizards_webfunc.php',
        './typo3/sysext/func_wizards/ext_emconf.php',
        './typo3/sysext/func_wizards/ext_icon.gif',
        './typo3/sysext/func_wizards/ext_tables.php',
        './typo3/sysext/info_pagetsconfig/class.tx_infopagetsconfig_webinfo.php',
        './typo3/sysext/info_pagetsconfig/cshimages/img_1.png',
        './typo3/sysext/info_pagetsconfig/cshimages/img_2.png',
        './typo3/sysext/info_pagetsconfig/cshimages/img_3.png',
        './typo3/sysext/info_pagetsconfig/cshimages/img_4.png',
        './typo3/sysext/info_pagetsconfig/cshimages/img_5.png',
        './typo3/sysext/info_pagetsconfig/doc/TODO.txt',
        './typo3/sysext/info_pagetsconfig/ext_emconf.php',
        './typo3/sysext/info_pagetsconfig/ext_icon.gif',
        './typo3/sysext/info_pagetsconfig/ext_tables.php',
        './typo3/sysext/install/ext_emconf.php',
        './typo3/sysext/install/ext_icon.gif',
        './typo3/sysext/install/ext_tables.php',
        './typo3/sysext/install/imgs/blackwhite_mask.gif',
        './typo3/sysext/install/imgs/combine_back.jpg',
        './typo3/sysext/install/imgs/combine_mask.jpg',
        './typo3/sysext/install/imgs/greenback.gif',
        './typo3/sysext/install/imgs/jesus2_transp.gif',
        './typo3/sysext/install/imgs/jesus2_transp.png',
        './typo3/sysext/install/imgs/jesus.bmp',
        './typo3/sysext/install/imgs/jesus.gif',
        './typo3/sysext/install/imgs/jesus.jpg',
        './typo3/sysext/install/imgs/jesus.pcx',
        './typo3/sysext/install/imgs/jesus.png',
        './typo3/sysext/install/imgs/jesus.tga',
        './typo3/sysext/install/imgs/jesus.tif',
        './typo3/sysext/install/imgs/pdf_from_imagemagick.pdf',
        './typo3/sysext/install/imgs/typo3logotype.ai',
        './typo3/sysext/install/mod/class.tx_install.php',
        './typo3/sysext/install/mod/clear.gif',
        './typo3/sysext/install/mod/conf.php',
        './typo3/sysext/install/mod/install.gif',
        './typo3/sysext/install/verify_imgs/install_44f1273ab1.jpg',
        './typo3/sysext/install/verify_imgs/install_48784f637a.gif',
        './typo3/sysext/install/verify_imgs/install_48784f637a.png',
        './typo3/sysext/install/verify_imgs/install_a8f7a333c8.gif',
        './typo3/sysext/install/verify_imgs/install_a8f7a333c8.png',
        './typo3/sysext/install/verify_imgs/install_d1fa76faad.gif',
        './typo3/sysext/install/verify_imgs/install_d1fa76faad.png',
        './typo3/sysext/install/verify_imgs/install_f6b0cedc4d.gif',
        './typo3/sysext/install/verify_imgs/install_f6b0cedc4d.png',
        './typo3/sysext/install/verify_imgs/install_fcaf26c521.jpg',
        './typo3/sysext/install/verify_imgs/install_fe1e67e805.gif',
        './typo3/sysext/install/verify_imgs/install_fe1e67e805.png',
        './typo3/sysext/install/verify_imgs/install_read_ai.jpg',
        './typo3/sysext/install/verify_imgs/install_read_bmp.jpg',
        './typo3/sysext/install/verify_imgs/install_read_gif.jpg',
        './typo3/sysext/install/verify_imgs/install_read_jpg.jpg',
        './typo3/sysext/install/verify_imgs/install_read_pcx.jpg',
        './typo3/sysext/install/verify_imgs/install_read_pdf.jpg',
        './typo3/sysext/install/verify_imgs/install_read_png.jpg',
        './typo3/sysext/install/verify_imgs/install_read_tga.jpg',
        './typo3/sysext/install/verify_imgs/install_read_tif.jpg',
        './typo3/sysext/install/verify_imgs/install_scale_gif.gif',
        './typo3/sysext/install/verify_imgs/install_scale_jpg.jpg',
        './typo3/sysext/install/verify_imgs/install_scale_png.png',
        './typo3/sysext/install/verify_imgs/install_write_gif.gif',
        './typo3/sysext/install/verify_imgs/install_write_png.png',
        './typo3/sysext/lang/cshimages/be_groups_10.png',
        './typo3/sysext/lang/cshimages/be_groups_11.png',
        './typo3/sysext/lang/cshimages/be_groups_12.png',
        './typo3/sysext/lang/cshimages/be_groups_13.png',
        './typo3/sysext/lang/cshimages/be_groups_14.png',
        './typo3/sysext/lang/cshimages/be_groups_15.png',
        './typo3/sysext/lang/cshimages/be_groups_16.png',
        './typo3/sysext/lang/cshimages/be_groups_17.png',
        './typo3/sysext/lang/cshimages/be_groups_18.png',
        './typo3/sysext/lang/cshimages/be_groups_19.png',
        './typo3/sysext/lang/cshimages/be_groups_1.png',
        './typo3/sysext/lang/cshimages/be_groups_20.png',
        './typo3/sysext/lang/cshimages/be_groups_2.png',
        './typo3/sysext/lang/cshimages/be_groups_3.png',
        './typo3/sysext/lang/cshimages/be_groups_4.png',
        './typo3/sysext/lang/cshimages/be_groups_5.png',
        './typo3/sysext/lang/cshimages/be_groups_6.png',
        './typo3/sysext/lang/cshimages/be_groups_7.png',
        './typo3/sysext/lang/cshimages/be_groups_8.png',
        './typo3/sysext/lang/cshimages/be_groups_9.png',
        './typo3/sysext/lang/cshimages/beuser_1.png',
        './typo3/sysext/lang/cshimages/beuser_2.png',
        './typo3/sysext/lang/cshimages/beuser_3.png',
        './typo3/sysext/lang/cshimages/beuser_4.png',
        './typo3/sysext/lang/cshimages/core_10.png',
        './typo3/sysext/lang/cshimages/core_11.png',
        './typo3/sysext/lang/cshimages/core_12.png',
        './typo3/sysext/lang/cshimages/core_13.png',
        './typo3/sysext/lang/cshimages/core_14.png',
        './typo3/sysext/lang/cshimages/core_15.png',
        './typo3/sysext/lang/cshimages/core_16.png',
        './typo3/sysext/lang/cshimages/core_17.png',
        './typo3/sysext/lang/cshimages/core_18.png',
        './typo3/sysext/lang/cshimages/core_19.png',
        './typo3/sysext/lang/cshimages/core_1.png',
        './typo3/sysext/lang/cshimages/core_20.png',
        './typo3/sysext/lang/cshimages/core_21.png',
        './typo3/sysext/lang/cshimages/core_22.png',
        './typo3/sysext/lang/cshimages/core_23.png',
        './typo3/sysext/lang/cshimages/core_24.png',
        './typo3/sysext/lang/cshimages/core_25.png',
        './typo3/sysext/lang/cshimages/core_26.png',
        './typo3/sysext/lang/cshimages/core_27.png',
        './typo3/sysext/lang/cshimages/core_28.png',
        './typo3/sysext/lang/cshimages/core_29.png',
        './typo3/sysext/lang/cshimages/core_2.png',
        './typo3/sysext/lang/cshimages/core_30.png',
        './typo3/sysext/lang/cshimages/core_31.png',
        './typo3/sysext/lang/cshimages/core_32.png',
        './typo3/sysext/lang/cshimages/core_33.png',
        './typo3/sysext/lang/cshimages/core_34.png',
        './typo3/sysext/lang/cshimages/core_35.png',
        './typo3/sysext/lang/cshimages/core_36.png',
        './typo3/sysext/lang/cshimages/core_37.png',
        './typo3/sysext/lang/cshimages/core_38.png',
        './typo3/sysext/lang/cshimages/core_39.png',
        './typo3/sysext/lang/cshimages/core_3.png',
        './typo3/sysext/lang/cshimages/core_40.png',
        './typo3/sysext/lang/cshimages/core_41.png',
        './typo3/sysext/lang/cshimages/core_42.png',
        './typo3/sysext/lang/cshimages/core_43.png',
        './typo3/sysext/lang/cshimages/core_44.png',
        './typo3/sysext/lang/cshimages/core_46.png',
        './typo3/sysext/lang/cshimages/core_47.png',
        './typo3/sysext/lang/cshimages/core_48.png',
        './typo3/sysext/lang/cshimages/core_49.png',
        './typo3/sysext/lang/cshimages/core_4.png',
        './typo3/sysext/lang/cshimages/core_50.png',
        './typo3/sysext/lang/cshimages/core_51.png',
        './typo3/sysext/lang/cshimages/core_52.png',
        './typo3/sysext/lang/cshimages/core_53.png',
        './typo3/sysext/lang/cshimages/core_54.png',
        './typo3/sysext/lang/cshimages/core_55.png',
        './typo3/sysext/lang/cshimages/core_56.png',
        './typo3/sysext/lang/cshimages/core_57.png',
        './typo3/sysext/lang/cshimages/core_58.png',
        './typo3/sysext/lang/cshimages/core_59.png',
        './typo3/sysext/lang/cshimages/core_5.png',
        './typo3/sysext/lang/cshimages/core_60.png',
        './typo3/sysext/lang/cshimages/core_61.png',
        './typo3/sysext/lang/cshimages/core_62.png',
        './typo3/sysext/lang/cshimages/core_63.png',
        './typo3/sysext/lang/cshimages/core_64.png',
        './typo3/sysext/lang/cshimages/core_65.png',
        './typo3/sysext/lang/cshimages/core_67.png',
        './typo3/sysext/lang/cshimages/core_68.png',
        './typo3/sysext/lang/cshimages/core_69.png',
        './typo3/sysext/lang/cshimages/core_6.png',
        './typo3/sysext/lang/cshimages/core_70.png',
        './typo3/sysext/lang/cshimages/core_7.png',
        './typo3/sysext/lang/cshimages/core_8.png',
        './typo3/sysext/lang/cshimages/core_9.png',
        './typo3/sysext/lang/cshimages/em_10.png',
        './typo3/sysext/lang/cshimages/em_11.png',
        './typo3/sysext/lang/cshimages/em_12.png',
        './typo3/sysext/lang/cshimages/em_1.png',
        './typo3/sysext/lang/cshimages/em_2.png',
        './typo3/sysext/lang/cshimages/em_3.png',
        './typo3/sysext/lang/cshimages/em_4.png',
        './typo3/sysext/lang/cshimages/em_5.png',
        './typo3/sysext/lang/cshimages/em_6.png',
        './typo3/sysext/lang/cshimages/em_7.png',
        './typo3/sysext/lang/cshimages/em_8.png',
        './typo3/sysext/lang/cshimages/em_9.png',
        './typo3/sysext/lang/cshimages/filemount_1.png',
        './typo3/sysext/lang/cshimages/login.png',
        './typo3/sysext/lang/cshimages/pages_1.png',
        './typo3/sysext/lang/cshimages/pages_2.png',
        './typo3/sysext/lang/cshimages/pages_3.png',
        './typo3/sysext/lang/cshimages/pages_4.png',
        './typo3/sysext/lang/cshimages/pages_5.png',
        './typo3/sysext/lang/cshimages/pages_6.png',
        './typo3/sysext/lang/cshimages/pages_7.png',
        './typo3/sysext/lang/cshimages/pages_8.png',
        './typo3/sysext/lang/cshimages/pagetree_overview_10.png',
        './typo3/sysext/lang/cshimages/pagetree_overview_11.png',
        './typo3/sysext/lang/ext_emconf.php',
        './typo3/sysext/lang/lang.php',
        './typo3/sysext/README.txt',
        './typo3/sysext/setup/cshimages/lang.png',
        './typo3/sysext/setup/cshimages/rte.png',
        './typo3/sysext/setup/cshimages/setup10.png',
        './typo3/sysext/setup/cshimages/setup11.png',
        './typo3/sysext/setup/cshimages/setup12.png',
        './typo3/sysext/setup/cshimages/setup1.png',
        './typo3/sysext/setup/cshimages/setup2.png',
        './typo3/sysext/setup/cshimages/setup3.png',
        './typo3/sysext/setup/cshimages/setup4.png',
        './typo3/sysext/setup/cshimages/setup5.png',
        './typo3/sysext/setup/cshimages/setup6.png',
        './typo3/sysext/setup/cshimages/setup7.png',
        './typo3/sysext/setup/cshimages/setup8.png',
        './typo3/sysext/setup/cshimages/setup9.png',
        './typo3/sysext/setup/ext_emconf.php',
        './typo3/sysext/setup/ext_icon.gif',
        './typo3/sysext/setup/ext_tables.php',
        './typo3/sysext/setup/mod/clear.gif',
        './typo3/sysext/setup/mod/conf.php',
        './typo3/sysext/setup/mod/index.php',
        './typo3/sysext/setup/mod/setup.gif',
        './typo3/sysext/tsconfig_help/doc/TODO.txt',
        './typo3/sysext/tsconfig_help/ext_emconf.php',
        './typo3/sysext/tsconfig_help/ext_icon.gif',
        './typo3/sysext/tsconfig_help/ext_tables.sql',
        './typo3/sysext/tsconfig_help/ext_tables_static+adt.sql',
        './typo3/sysext/wizard_crpages/class.tx_wizardcrpages_webfunc_2.php',
        './typo3/sysext/wizard_crpages/cshimages/wizards_1.png',
        './typo3/sysext/wizard_crpages/cshimages/wizards_2.png',
        './typo3/sysext/wizard_crpages/ext_emconf.php',
        './typo3/sysext/wizard_crpages/ext_icon.gif',
        './typo3/sysext/wizard_crpages/ext_tables.php',
        './typo3/sysext/wizard_sortpages/class.tx_wizardsortpages_webfunc_2.php',
        './typo3/sysext/wizard_sortpages/cshimages/wizards_1.png',
        './typo3/sysext/wizard_sortpages/ext_emconf.php',
        './typo3/sysext/wizard_sortpages/ext_icon.gif',
        './typo3/sysext/wizard_sortpages/ext_tables.php',
        './typo3/tce_db.php',
        './typo3/tce_file.php',
        './typo3/template.php',
        './typo3/wizard_add.php',
        './typo3/wizard_colorpicker.php',
        './typo3/wizard_edit.php',
        './typo3/wizard_forms.php',
        './typo3/wizard_list.php',
        './typo3/wizard_rte.php',
        './typo3/wizard_table.php',
        './typo3/wizard_tsconfig.php',
        './uploads/index.html',
    ]


    def get_version(self,path):

        # Typo3 < 6.0
        conf_path = os.path.join(path,'t3lib/config_default.php')
        if os.path.exists(conf_path):
            cont = open(conf_path).read()
            m = RE_VERSION_OLD.search(cont)
            if m is not None:
                return (m.group(1))

        # Typo3 >= 6.0
        conf_path = os.path.join(path,'typo3/sysext/core/Classes/Core/SystemEnvironmentBuilder.php')
        if os.path.exists(conf_path):
            cont = open(conf_path).read()
            m = RE_VERSION.search(cont)
            if m is not None:
                return (m.group(1))

    # gets activated typo3 extensions from localconf.php
    def get_activated_plugins(self, path):

        conf_path = os.path.join(path,'typo3conf/localconf.php')
        if os.path.exists(conf_path):

            php_code = open(conf_path).read()

            # Modify the PHP Code to output infos
            php_code = self.php_change_code(
                php_code,
                prepend="define('TYPO3_MODE',1);",
                append="echo $TYPO3_CONF_VARS['EXT']['extList'];"
            )

            mods = self.exec_php_code(php_code)
            if mods != None:
                ret_val={}
                for mod in mods.split(','):
                    ret_val[mod] = {}
                return ret_val

        return {}


    # fetches the installed plugins and theirs versions
    def get_installed_plugins(self, path):

        # return dict with extensions
        ret_val = {}

        # Path to extension dir
        exts_path = os.path.join(path,'typo3conf/ext/')

        # If is dir
        if os.path.isdir(exts_path):
            for ext in os.listdir(exts_path):
                ext_path = os.path.join(exts_path,ext)

                # Skip files
                if not os.path.isdir(ext_path):
                    continue

                conf_path = os.path.join(ext_path,'ext_emconf.php')
                if os.path.isfile(conf_path):
                    php_code = open(conf_path).read()

                    # Modify the PHP Code to output infos
                    php_code = self.php_change_code(
                        php_code,
                        prepend="$_EXTKEY = 0;",
                        append="echo $EM_CONF[0]['version'];"
                    )

                    version = self.exec_php_code(php_code)

                ret_val[ext]={}

                if version != None:
                    ret_val[ext]['version']=version.strip()

        return ret_val


    # return active plugins and their version
    def get_plugins(self, path):

        # Activated Plugins list
        active_plugins = self.get_activated_plugins(path).keys()

        # return dictionariy
        ret_val = []

        # installed plugins dict
        installed_plugins = self.get_installed_plugins(path)

        # Output only active plugins as list of plugin dicts
        for plugin in installed_plugins.keys():
            if plugin in active_plugins:
                plugin_dict = {'name' : plugin}
                plugin_dict.update(installed_plugins[plugin])
                ret_val.append(plugin_dict)

        return ret_val
