# -*- coding: utf-8 -*-
#
# This file is part of NINJA-IDE (http://ninja-ide.org).
#
# NINJA-IDE is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# any later version.
#
# NINJA-IDE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NINJA-IDE; If not, see <http://www.gnu.org/licenses/>.
from __future__ import absolute_import

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QKeySequence
# from PyQt5.QtCore import SIGNAL
from PyQt5.QtCore import QObject
from PyQt5.QtCore import Qt

from ninja_ide import resources
from ninja_ide.core import settings
from ninja_ide.gui import actions


class MenuSource(QObject):

    def __init__(self, menuSource):
        QObject.__init__(self)

        indentMoreAction = menuSource.addAction(
            QIcon(resources.IMAGES['indent-more']),
            (self.tr("Indent More (%s)") %
                QKeySequence(Qt.Key_Tab).toString(QKeySequence.NativeText)))
        indentLessAction = menuSource.addAction(
            QIcon(resources.IMAGES['indent-less']),
            (self.tr("Indent Less (%s)") %
                resources.get_shortcut("Indent-less").toString(
                    QKeySequence.NativeText)))
        menuSource.addSeparator()
        commentAction = menuSource.addAction(
            QIcon(resources.IMAGES['comment-code']),
            (self.tr("Comment (%s)") %
                resources.get_shortcut("Comment").toString(
                    QKeySequence.NativeText)))
        unCommentAction = menuSource.addAction(
            QIcon(resources.IMAGES['uncomment-code']),
            (self.tr("Uncomment (%s)") %
                resources.get_shortcut("Uncomment").toString(
                    QKeySequence.NativeText)))
        horizontalLineAction = menuSource.addAction(
            (self.tr("Insert Horizontal Line (%s)") %
                resources.get_shortcut("Horizontal-line").toString(
                    QKeySequence.NativeText)))
        titleCommentAction = menuSource.addAction(
            (self.tr("Insert Title Comment (%s)") %
                resources.get_shortcut("Title-comment").toString(
                    QKeySequence.NativeText)))
        countCodeLinesAction = menuSource.addAction(
            self.tr("Count Code Lines"))
        menuSource.addSeparator()
#        tellTaleAction = menuSource.addAction(
#            self.tr("Tell me a Tale of Code"))
#        tellTaleAction.setEnabled(False)
        goToDefinitionAction = menuSource.addAction(
            QIcon(resources.IMAGES['go-to-definition']),
            (self.tr("Go To Definition (%s or %s+Click)") %
                (resources.get_shortcut("Go-to-definition").toString(
                    QKeySequence.NativeText),
                settings.OS_KEY)))
        insertImport = menuSource.addAction(
            QIcon(resources.IMAGES['insert-import']),
            (self.tr("Insert &Import (%s)") %
                resources.get_shortcut("Import").toString(
                    QKeySequence.NativeText)))
        menu_debugging = menuSource.addMenu(self.tr("Debugging Tricks"))
        insertPrints = menu_debugging.addAction(
            self.tr("Insert Prints per selected line."))
        insertPdb = menu_debugging.addAction(
            self.tr("Insert pdb.set_trace()"))
#        organizeImportsAction = menuSource.addAction(
#            self.tr("&Organize Imports"))
#        removeUnusedImportsAction = menuSource.addAction(
#            self.tr("Remove Unused &Imports"))
#        extractMethodAction = menuSource.addAction(
#            self.tr("Extract selected &code as Method"))
        menuSource.addSeparator()
        removeTrailingSpaces = menuSource.addAction(
            self.tr("&Remove Trailing Spaces"))
        replaceTabsSpaces = menuSource.addAction(
            self.tr("Replace Tabs With &Spaces"))
        moveUp = menuSource.addAction((self.tr("Move &Up (%s)") %
            resources.get_shortcut("Move-up").toString(
                QKeySequence.NativeText)))
        moveDown = menuSource.addAction((self.tr("Move &Down (%s)") %
            resources.get_shortcut("Move-down").toString(
                QKeySequence.NativeText)))
        duplicate = menuSource.addAction(
            (self.tr("Duplica&te (%s)") %
                resources.get_shortcut("Duplicate").toString(
                    QKeySequence.NativeText)))
        remove = menuSource.addAction(
            (self.tr("&Remove Line (%s)") %
                resources.get_shortcut("Remove-line").toString(
                    QKeySequence.NativeText)))

        self.toolbar_items = {
            'indent-more': indentMoreAction,
            'indent-less': indentLessAction,
            'comment': commentAction,
            'uncomment': unCommentAction,
            'go-to-definition': goToDefinitionAction,
            'insert-import': insertImport}

        # self.connect(goToDefinitionAction, SIGNAL("triggered()"),
        #     actions.Actions().editor_go_to_definition)
        goToDefinitionAction.triggered.connect(actions.Actions().editor_go_to_definition)
        # self.connect(countCodeLinesAction, SIGNAL("triggered()"),
        #     actions.Actions().count_file_code_lines)
        countCodeLinesAction.triggered.connect(actions.Actions().count_file_code_lines)
        # self.connect(insertImport, SIGNAL("triggered()"),
        #     actions.Actions().import_from_everywhere)
        insertImport.triggered.connect(actions.Actions().import_from_everywhere)
        # self.connect(indentMoreAction, SIGNAL("triggered()"),
        #     actions.Actions().editor_indent_more)
        indentLessAction.triggered.connect(actions.Actions().editor_indent_less)
        # self.connect(indentLessAction, SIGNAL("triggered()"),
        #     actions.Actions().editor_indent_less)
        commentAction.triggered.connect(actions.Actions().editor_comment)
        # self.connect(commentAction, SIGNAL("triggered()"),
        #     actions.Actions().editor_comment)
        unCommentAction.triggered.connect(actions.Actions().editor_uncomment)
        # self.connect(unCommentAction, SIGNAL("triggered()"),
        #     actions.Actions().editor_uncomment)
        horizontalLineAction.triggered.connect(actions.Actions().editor_insert_horizontal_line)
        # self.connect(horizontalLineAction, SIGNAL("triggered()"),
        #     actions.Actions().editor_insert_horizontal_line)
        titleCommentAction.triggered.connect(actions.Actions().editor_insert_title_comment)
        # self.connect(titleCommentAction, SIGNAL("triggered()"),
        #     actions.Actions().editor_insert_title_comment)

#        QObject.connect(removeUnusedImportsAction, SIGNAL("triggered()"),
#        lambda: self._main._central.obtain_editor().remove_unused_imports())
##        QObject.connect(addMissingImportsAction, SIGNAL("triggered()"),
#        lambda: self._main._central.obtain_editor().add_missing_imports())
#        QObject.connect(organizeImportsAction, SIGNAL("triggered()"),
#        lambda: self._main._central.obtain_editor().organize_imports())
#        QObject.connect(extractMethodAction, SIGNAL("triggered()"),
#        lambda: self._main._central.obtain_editor().extract_method())
        # self.connect(moveUp, SIGNAL("triggered()"),
        #     actions.Actions().editor_move_up)
        moveUp.triggered.connect(actions.Actions().editor_move_up)
        # self.connect(moveDown, SIGNAL("triggered()"),
        #     actions.Actions().editor_move_down)
        moveDown.triggered.connect(actions.Actions().editor_move_down)
        # self.connect(duplicate, SIGNAL("triggered()"),
        #     actions.Actions().editor_duplicate)
        duplicate.triggered.connect(actions.Actions().editor_duplicate)
        # self.connect(replaceTabsSpaces, SIGNAL("triggered()"),
        #     actions.Actions().editor_replace_tabs_with_spaces)
        replaceTabsSpaces.triggered.connect(actions.Actions().editor_replace_tabs_with_spaces)
        # self.connect(removeTrailingSpaces, SIGNAL("triggered()"),
        #     actions.Actions().editor_remove_trailing_spaces)
        removeTrailingSpaces.triggered.connect(actions.Actions().editor_remove_trailing_spaces)
        # self.connect(remove, SIGNAL("triggered()"),
        #     actions.Actions().editor_remove_line)
        remove.triggered.connect(actions.Actions().editor_remove_line)
        # self.connect(insertPrints, SIGNAL("triggered()"),
        #     actions.Actions().editor_insert_debugging_prints)
        insertPrints.triggered.connect(actions.Actions().editor_insert_debugging_prints)
        # self.connect(insertPdb, SIGNAL("triggered()"),
        #     actions.Actions().editor_insert_pdb)
        insertPdb.triggered.connect(actions.Actions().editor_insert_pdb)
