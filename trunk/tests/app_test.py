#!/usr/bin/env python
# Copyright 2008 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for app.py ."""




import os
import shutil
import socket

import mox

from google.apputils import basetest

from google.apputils import app
import gflags as flags

FLAGS = flags.FLAGS


class TestFunctions(basetest.TestCase):
  def setUp(self):
    self.mox = mox.Mox()
    # recreate the FLAGS.test_tmpdir
    shutil.rmtree(FLAGS.test_tmpdir)
    os.makedirs(FLAGS.test_tmpdir)

  def tearDown(self):
    self.mox.UnsetStubs()

  def testInstallExceptionHandler(self):
    self.assertRaises(TypeError, app.InstallExceptionHandler, 1)


if __name__ == '__main__':
  basetest.main()
