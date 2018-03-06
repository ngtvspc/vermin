from .multidict import multidict

# Module requirements: name -> min version per major or None if N.A.
MOD_REQS = {
  "ConfigParser": (2.0, None),
  "HTMLParser": (2.2, None),
  "Queue": (2.0, None),
  "SocketServer": (2.0, None),
  "__builtin__": (2.0, None),
  "_markupbase": (None, 3.0),
  "_winreg": (2.0, None),
  "abc": (2.6, 3.0),
  "argparse": (2.7, 3.2),
  "ast": (2.6, 3.0),
  "asyncio": (None, 3.4),
  "builtins": (None, 3.0),
  "configparser": (None, 3.0),
  "copy_reg": (2.0, None),
  "copyreg": (None, 3.0),
  "dbm.io": (None, 3.0),
  "dbm.ndbm": (None, 3.0),
  "dbm.os": (None, 3.0),
  "dbm.struct": (None, 3.0),
  "dbm.sys": (None, 3.0),
  "dbm.whichdb": (None, 3.0),
  "faulthandler": (None, 3.3),
  "hashlib": (2.5, 3.0),
  "html": (None, 3.0),
  "htmlentitydefs": (2.0, None),
  "http": (None, 3.0),
  "ipaddress": (None, 3.3),
  "markupbase": (2.0, None),
  "md5": (2.0, None),
  "multiprocessing": (2.6, 3.0),
  "new": (2.0, None),
  "queue": (None, 3.0),
  "repr": (2.0, None),
  "reprlib": (None, 3.0),
  "secrets": (None, 3.6),
  "sets": (2.0, None),
  "socketserver": (None, 3.0),
  "string.letters": (2.0, None),
  "string.lowercase": (2.0, None),
  "string.uppercase": (2.0, None),
  "tkinter": (None, 3.0),
  "tracemalloc": (None, 3.4),
  "typing": (None, 3.5),
  "unittest": (2.1, 3.0),
  "urllib2": (2.0, None),
  "winreg": (None, 3.0),
  "xmlrpc": (None, 3.0),
}

# Module member requirements: member -> (module, requirements)
MOD_MEM_REQS = multidict((
  # Classes
  ("ABC", ("abc", (None, 3.4))),
  ("AsyncGenerator", ("typing", (None, 3.6))),
  ("Barrier", ("multiprocessing", (None, 3.3))),
  ("ChainMap", ("typing", (None, 3.6))),
  ("ClassVar", ("typing", (None, 3.5))),
  ("Collection", ("typing", (None, 3.6))),
  ("ContextManager", ("typing", (None, 3.6))),
  ("Counter", ("typing", (None, 3.6))),
  ("Deque", ("typing", (None, 3.6))),
  ("DomainFilter", ("tracemalloc", (None, 3.6))),
  ("PathLike", ("os", (None, 3.6))),
  ("Text", ("typing", (None, 3.6))),
  ("TextTestResult", ("unittest", (2.7, 3.0))),
  ("terminal_size", ("os", (None, 3.3))),
  ("timezone", ("datetime", (None, 3.2))),

  # Functions
  ("NewType", ("typing", (None, 3.5))),
  ("addCleanup", ("unittest.TestCase", (2.7, 3.0))),
  ("addTypeEqualityFunc", ("unittest.TestCase", (2.7, 3.0))),
  ("assertDictContainsSubset", ("unittest.TestCase", (2.7, 3.0))),
  ("assertDictEqual", ("unittest.TestCase", (2.7, 3.0))),
  ("assertGreater", ("unittest.TestCase", (2.7, 3.0))),
  ("assertGreaterEqual", ("unittest.TestCase", (2.7, 3.0))),
  ("assertIn", ("unittest.TestCase", (2.7, 3.0))),
  ("assertIs", ("unittest.TestCase", (2.7, 3.0))),
  ("assertIsInstance", ("unittest.TestCase", (2.7, 3.0))),
  ("assertIsNone", ("unittest.TestCase", (2.7, 3.0))),
  ("assertIsNot", ("unittest.TestCase", (2.7, 3.0))),
  ("assertIsNotNone", ("unittest.TestCase", (2.7, 3.0))),
  ("assertItemsEqual", ("unittest.TestCase", (2.7, 3.0))),
  ("assertLess", ("unittest.TestCase", (2.7, 3.0))),
  ("assertLessEqual", ("unittest.TestCase", (2.7, 3.0))),
  ("assertListEqual", ("unittest.TestCase", (2.7, 3.0))),
  ("assertMultilineEqual", ("unittest.TestCase", (2.7, 3.0))),
  ("assertNotIn", ("unittest.TestCase", (2.7, 3.0))),
  ("assertNotIsInstance", ("unittest.TestCase", (2.7, 3.0))),
  ("assertNotRegexpMatches", ("unittest.TestCase", (2.7, 3.0))),
  ("assertRaisesRegexp", ("unittest.TestCase", (2.7, 3.0))),
  ("assertRegexpMatches", ("unittest.TestCase", (2.7, 3.0))),
  ("assertSequenceEqual", ("unittest.TestCase", (2.7, 3.0))),
  ("assertSetEqual", ("unittest.TestCase", (2.7, 3.0))),
  ("assertTupleEqual", ("unittest.TestCase", (2.7, 3.0))),
  ("commonpath", ("os.path", (None, 3.5))),
  ("discover", ("unittest.TestLoader", (2.7, 3.0))),
  ("doCleanup", ("unittest.TestCase", (2.7, 3.0))),
  ("exc_clear", ("sys", (2.3, None))),
  ("fsdecode", ("os", (None, 3.2))),
  ("fsencode", ("os", (None, 3.2))),
  ("fspath", ("os", (None, 3.6))),
  ("get_all_start_methods", ("multiprocessing", (None, 3.4))),
  ("get_blocking", ("os", (None, 3.5))),
  ("get_context", ("multiprocessing", (None, 3.4))),
  ("get_exec_path", ("os", (None, 3.2))),
  ("get_handle_inheritable", ("os", (None, 3.4))),
  ("get_inheritable", ("os", (None, 3.4))),
  ("get_start_method", ("multiprocessing", (None, 3.4))),
  ("get_terminal_size", ("os", (None, 3.3))),
  ("getcheckinterval", ("sys", (2.3, 3.0))),
  ("getctime", ("os.path", (2.3, 3.0))),
  ("getdefaultencoding", ("sys", (2.0, 3.0))),
  ("getdlopenflags", ("sys", (2.2, 3.0))),
  ("getenvb", ("os", (None, 3.2))),
  ("getfilesystemencoding", ("sys", (2.3, 3.0))),
  ("getgrouplist", ("os", (None, 3.3))),
  ("getpgid", ("os", (2.3, 3.0))),
  ("getpriority", ("os", (None, 3.3))),
  ("getprofile", ("sys", (2.6, 3.0))),
  ("getresgid", ("os", (2.7, 3.0))),
  ("getresuid", ("os", (2.7, 3.0))),
  ("getsid", ("os", (2.4, 3.0))),
  ("getsizeof", ("sys", (2.6, 3.0))),
  ("gettrace", ("sys", (2.6, 3.0))),
  ("getwindowsversion", ("sys", (2.3, 3.0))),
  ("initgroups", ("os", (2.7, 3.2))),
  ("ismount", ("os.path", (None, 3.4))),
  ("lexists", ("os.path", (2.4, 3.0))),
  ("lockf", ("os", (None, 3.3))),
  ("longMessage", ("unittest.TestCase", (2.7, 3.0))),
  ("maxDiff", ("unittest.TestCase", (2.7, 3.0))),
  ("pbkdf2_hmac", ("hashlib", (2.7, 3.4))),
  ("pipe2", ("os", (None, 3.3))),
  ("posix_fadvise", ("os", (None, 3.3))),
  ("posix_fallocate", ("os", (None, 3.3))),
  ("pread", ("os", (None, 3.3))),
  ("pwrite", ("os", (None, 3.3))),
  ("readv", ("os", (None, 3.3))),
  ("realpath", ("os.path", (2.6, 3.0))),
  ("scrypt", ("hashlib", (None, 3.6))),
  ("sendfile", ("os", (None, 3.3))),
  ("set_blocking", ("os", (None, 3.5))),
  ("set_handle_inheritable", ("os", (None, 3.4))),
  ("set_inheritable", ("os", (None, 3.4))),
  ("set_start_method", ("multiprocessing", (None, 3.4))),
  ("setgroups", ("os", (2.2, 3.0))),
  ("setpriority", ("os", (None, 3.3))),
  ("setresgid", ("os", (2.7, 3.2))),
  ("setresuid", ("os", (2.7, 3.2))),
  ("starmap", ("multiprocessing.Pool", (None, 3.3))),
  ("starmap_async", ("multiprocessing.Pool", (None, 3.3))),
  ("startTestRun", ("unittest.TestResult", (2.7, 3.0))),
  ("stopTestRun", ("unittest.TestResult", (2.7, 3.0))),
  ("timestamp", ("datetime.datetime", (None, 3.3))),
  ("total_seconds", ("datetime.timedelta", (None, 3.2))),
  ("wait", ("multiprocessing.connection", (None, 3.3))),
  ("writev", ("os", (None, 3.3))),

  # Variables and Constants
  ("F_LOCK", ("os", (None, 3.3))),
  ("F_TEST", ("os", (None, 3.3))),
  ("F_TLOCK", ("os", (None, 3.3))),
  ("F_ULOCK", ("os", (None, 3.3))),
  ("O_CLOEXEC", ("os", (None, 3.3))),
  ("O_PATH", ("os", (None, 3.4))),
  ("O_TMPFILE", ("os", (None, 3.4))),
  ("POSIX_FADV_DONTNEED", ("os", (None, 3.3))),
  ("POSIX_FADV_NOREUSE", ("os", (None, 3.3))),
  ("POSIX_FADV_NORMAL", ("os", (None, 3.3))),
  ("POSIX_FADV_RANDOM", ("os", (None, 3.3))),
  ("POSIX_FADV_SEQUENTIAL", ("os", (None, 3.3))),
  ("POSIX_FADV_WILLNEED", ("os", (None, 3.3))),
  ("PRIO_PGRP", ("os", (None, 3.3))),
  ("PRIO_PROCESS", ("os", (None, 3.3))),
  ("PRIO_USER", ("os", (None, 3.3))),
  ("SF_MNOWAIT", ("os", (None, 3.3))),
  ("SF_NODISKIO", ("os", (None, 3.3))),
  ("SF_SYNC", ("os", (None, 3.3))),
  ("TYPE_CHECKING", ("typing", (None, 3.5))),
  ("algorithms", ("hashlib", (2.7, None))),
  ("algorithms_available", ("hashlib", (2.7, 3.2))),
  ("algorithms_guaranteed", ("hashlib", (2.7, 3.2))),
  ("api_version", ("sys", (2.3, 3.0))),
  ("buffer", ("unittest.TestResult", (2.7, 3.0))),
  ("environb", ("os", (None, 3.2))),
  ("failfast", ("unittest.TestResult", (2.7, 3.0))),
  ("flags", ("sys", (2.6, 3.0))),
  ("float_info", ("sys", (2.6, 3.0))),
  ("float_repr_style", ("sys", (2.7, 3.0))),
  ("fold", ("datetime.datetime", (None, 3.6))),
  ("is_global", ("ipaddress.IPv4Address", (None, 3.4))),
  ("is_global", ("ipaddress.IPv6Address", (None, 3.4))),
  ("long_info", ("sys", (2.7, None))),
  ("py3kwarning", ("sys", (2.6, None))),
  ("reverse_pointer", ("ipaddress.IPv4Address", (None, 3.5))),
  ("sentinel", ("multiprocessing.Process", (None, 3.3))),
  ("skipped", ("unittest.TestResult", (2.7, 3.0))),
  ("subversion", ("sys", (2.5, None))),
  ("supports_bytes_environ", ("os", (None, 3.2))),
  ("supports_unicode_filenames", ("os.path", (2.3, 3.0))),
  ("version_info", ("sys", (2.0, 3.0))),
))

# Keyword arguments requirements: (function, keyword argument) -> requirements
KWARGS_REQS = {
  ("Filter", "domain"): (None, 3.6),  # tracemalloc
  ("Pool", "context"): (None, 3.4),  # multiprocessing
  ("Pool", "maxtasksperchild"): (None, 3.2),  # multiprocessing
  ("PrettyPrinter", "compact"): (None, 3.4),  # pprint
  ("Process", "daemon"): (None, 3.3),  # multiprocessing
  ("access", "dir_fd"): (None, 3.3),  # os
  ("access", "effective_ids"): (None, 3.3),  # os
  ("access", "follow_symlinks"): (None, 3.3),  # os
  ("assertAlmostEqual", "delta"): (2.7, 3.0),  # unittest.TestCase
  ("assertNotAlmostEqual", "delta"): (2.7, 3.0),  # unittest.TestCase
  ("chflags", "follow_symlinks"): (None, 3.3),  # os
  ("chmod", "dir_fd"): (None, 3.3),  # os
  ("chmod", "follow_symlinks"): (None, 3.3),  # os
  ("chown", "dir_fd"): (None, 3.3),  # os
  ("chown", "follow_symlinks"): (None, 3.3),  # os
  ("combine", "tzinfo"): (None, 3.6),  # datetime.datetime
  ("datetime", "fold"): (None, 3.6),  # datetime.datetime
  ("dup2", "inheritable"): (None, 3.4),  # os
  ("isoformat", "timespec"): (None, 3.6),  # datetime.datetime
  ("link", "dst_dir_fd"): (None, 3.3),  # os
  ("link", "follow_symlinks"): (None, 3.3),  # os
  ("link", "src_dir_fd"): (None, 3.3),  # os
  ("open", "dir_fd"): (None, 3.3),  # os
  ("pformat", "compact"): (None, 3.4),  # pprint
  ("pprint", "compact"): (None, 3.4),  # pprint
  ("replace", "fold"): (None, 3.6),  # datetime.datetime
}

# datetime+time strftime/strptime requirements: directive -> requirements
STRFTIME_REQS = {
  "%G": (None, 3.6),
  "%V": (None, 3.6),
  "%f": (2.6, 3.0),
  "%u": (None, 3.6),
}