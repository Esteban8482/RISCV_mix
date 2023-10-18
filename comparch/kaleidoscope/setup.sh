#!/usr/bin/bash

export CLASSPATH=".:antlr-4.7-complete.jar:$CLASSPATH"

alias antlr4='java -Xmx500M -cp "$DIR/antlr-4.7-complete.jar:$CLASSPATH" org.antlr.v4.Tool'

alias grun='java org.antlr.v4.gui.TestRig'
