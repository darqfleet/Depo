#background color: base01
#font color: base01
template ='''
QMainWindow#main {
    background-color: $base00;
}
QListWidget {
    background-color: $base00;
    color:$base04;
}
QStatusBar {
    background-color: $base00;
    color:$base04;
}
QMenu {
    background-color: $base00;
    color:$base04;
}
QMenu::item:selected { /* when selected using mouse or keyboard */
    background: $base01;
}
QMenu::item:pressed {
    color: $base0D;
}
QWidget#default {
    background-color: $base00;
}
QMenuBar {
    background-color: $base00;
    color:$base04;
}
QMenuBar::item {
    padding: 1px 2px;
    background: transparent;
border-radius: 2px;
}

QMenuBar::item:selected { /* when selected using mouse or keyboard */
    background: $base01;
}

QMenuBar::item:pressed {
    color: $base0D;
}
QWidget#default {
    background-color: $base00;
}
QPushButton {
    background-color: $base00;
    color:$base04;
    border-style: solid;
    border-color: $base01;
    padding: 5px;
    border-width: 1px;
    border-radius: 5px;
    font: JetBrainsMonoNL-Bold;
}
QPushButton:pressed {
    background-color: $base01;
    padding: 5px;
    border-style: solid;
    border-width: 1px;
    border-radius: 5px;
    border-color: $base09;
    color: $base0D;}
'''
