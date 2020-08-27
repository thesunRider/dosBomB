#############################################################################
# Generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#  Aug 26, 2020 11:26:13 PM IST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) firebrick
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m46" -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 604x325+746+228
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1030
    wm minsize $top 148 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm deiconify $top
    wm title $top "dosBomB v1.01"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra45 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 575 
    vTcl:DefineAlias "$top.fra45" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra45
    label $site_3_0.lab48 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Coded by:} 
    vTcl:DefineAlias "$site_3_0.lab48" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab49 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text dosBomB 
    vTcl:DefineAlias "$site_3_0.lab49" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab50 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text v1.01 
    vTcl:DefineAlias "$site_3_0.lab50" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab51 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Suryasaradhi 
    vTcl:DefineAlias "$site_3_0.lab51" "Label4" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab52 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text picturlabel 
    vTcl:DefineAlias "$site_3_0.lab52" "Label5" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab48 \
        -in $site_3_0 -x 0 -relx 0.466 -y 0 -rely 0.132 -width 0 \
        -relwidth 0.141 -height 0 -relheight 0.342 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab49 \
        -in $site_3_0 -x 0 -relx 0.293 -y 0 -rely 0.282 -width 0 \
        -relwidth 0.141 -height 0 -relheight 0.366 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab50 \
        -in $site_3_0 -x 0 -relx 0.362 -y 0 -rely 0.563 -width 0 \
        -relwidth 0.072 -height 0 -relheight 0.366 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab51 \
        -in $site_3_0 -x 0 -relx 0.603 -y 0 -rely 0.141 -width 0 \
        -relwidth 0.155 -height 0 -relheight 0.366 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab52 \
        -in $site_3_0 -x 0 -relx 0.069 -y 0 -rely 0.282 -height 0 \
        -relheight 0.366 -anchor nw -bordermode ignore 
    menu $top.m46 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    $top.m46 add command \
        -command {#} -label File 
    $top.m46 add command \
        -command {#} -label Settings 
    $top.m46 add command \
        -command {#} -label About 
    $top.m46 add cascade \
        -menu "$top.m46.men56" -command {{}} -label NewCascade 
    set site_3_0 $top.m46
    menu $site_3_0.men56 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    $site_3_0.men56 add command \
        -command {#} -label NewCommand 
    ttk::style configure PC.TNotebook -background $vTcl(actual_gui_bg)
    ttk::style configure PC.TNotebook.Tab -background $vTcl(actual_gui_bg)
    ttk::style configure PC.TNotebook.Tab -foreground $vTcl(actual_gui_fg)
    ttk::style configure PC.TNotebook.Tab -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style layout PC.TNotebook.Tab {
                    Notebook.tab -children {
                        Notebook.padding -side top -children {
                            Notebook.focus -side top -children {
                                Notebook.text -side right
                                Notebook.image -side left
                            }
                        }
                    }
               }
    vTcl::widgets::ttk::pnotebook::createCmd $top.pNo47 \
        -width 300 -height 200 -style "PC.TNotebook" 
    vTcl:DefineAlias "$top.pNo47" "PNotebook1" vTcl:WidgetProc "Toplevel1" 1
    $top.pNo47 configure -style "PC.TNotebook"
    bind $top.pNo47 <Button-1> {
        _button_press
    }
    bind $top.pNo47 <ButtonRelease-1> {
        _button_release
    }
    bind $top.pNo47 <Motion> {
        _mouse_over
    }
    frame $top.pNo47.t1 \
        -borderwidth 20 -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$top.pNo47.t1" "PNotebook1_t2_1" vTcl:WidgetProc "Toplevel1" 1
    $top.pNo47 add $top.pNo47.t1 \
        -padding 0 -sticky nsew -state normal -text General -image image2 \
        -compound none -underline -1 
    set site_4_0  $top.pNo47.t1
    label $site_4_0.lab61 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text placerad 
    vTcl:DefineAlias "$site_4_0.lab61" "Label12" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $site_4_0.tLa62 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left \
        -text Description 
    vTcl:DefineAlias "$site_4_0.tLa62" "TLabel4" vTcl:WidgetProc "Toplevel1" 1
    text $site_4_0.tex63 \
        -background white -font TkTextFont -foreground black -height 100 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 264 -wrap word 
    $site_4_0.tex63 configure -font "TkTextFont"
    $site_4_0.tex63 insert end text
    vTcl:DefineAlias "$site_4_0.tex63" "Text2" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_0.but46 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$site_4_0.but46" "Button3" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.lab61 \
        -in $site_4_0 -x 0 -relx 0.036 -y 0 -rely 0.088 -width 0 \
        -relwidth 0.075 -height 0 -relheight 0.115 -anchor nw \
        -bordermode ignore 
    place $site_4_0.tLa62 \
        -in $site_4_0 -x 0 -relx 0.5 -y 0 -width 0 -relwidth 0.152 -height 0 \
        -relheight 0.104 -anchor nw -bordermode ignore 
    place $site_4_0.tex63 \
        -in $site_4_0 -x 0 -relx 0.5 -y 0 -rely 0.155 -width 0 \
        -relwidth 0.471 -height 0 -relheight 0.518 -anchor nw \
        -bordermode ignore 
    place $site_4_0.but46 \
        -in $site_4_0 -x 0 -relx 0.5 -y 0 -rely 0.725 -width 266 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    frame $top.pNo47.t0 \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$top.pNo47.t0" "PNotebook1_t1_2" vTcl:WidgetProc "Toplevel1" 1
    $top.pNo47 add $top.pNo47.t0 \
        -padding 0 -sticky nsew -state normal -text Scan -image image2 \
        -compound none -underline -1 
    set site_4_1  $top.pNo47.t0
    frame $top.pNo47.t2 \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$top.pNo47.t2" "PNotebook1_t3_3" vTcl:WidgetProc "Toplevel1" 1
    $top.pNo47 add $top.pNo47.t2 \
        -padding 0 -sticky nsew -state normal -text Flooder -image {} \
        -compound none -underline -1 
    set site_4_2  $top.pNo47.t2
    ttk::style configure PC.TNotebook -background $vTcl(actual_gui_bg)
    ttk::style configure PC.TNotebook.Tab -background $vTcl(actual_gui_bg)
    ttk::style configure PC.TNotebook.Tab -foreground $vTcl(actual_gui_fg)
    ttk::style configure PC.TNotebook.Tab -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style layout PC.TNotebook.Tab {
                    Notebook.tab -children {
                        Notebook.padding -side top -children {
                            Notebook.focus -side top -children {
                                Notebook.text -side right
                                Notebook.image -side left
                            }
                        }
                    }
               }
    vTcl::widgets::ttk::pnotebook::createCmd $site_4_2.pNo45 \
        -width 300 -height 200 -style "PC.TNotebook" 
    vTcl:DefineAlias "$site_4_2.pNo45" "PNotebook2" vTcl:WidgetProc "Toplevel1" 1
    $site_4_2.pNo45 configure -style "PC.TNotebook"
    bind $site_4_2.pNo45 <Button-1> {
        _button_press
    }
    bind $site_4_2.pNo45 <ButtonRelease-1> {
        _button_release
    }
    bind $site_4_2.pNo45 <Motion> {
        _mouse_over
    }
    frame $site_4_2.pNo45.t0 \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$site_4_2.pNo45.t0" "PNotebook2_t1_4" vTcl:WidgetProc "Toplevel1" 1
    $site_4_2.pNo45 add $site_4_2.pNo45.t0 \
        -padding 0 -sticky nsew -state normal -text {Syn Flood} -image image2 \
        -compound none -underline -1 
    set site_6_0  $site_4_2.pNo45.t0
    frame $site_4_2.pNo45.t2 \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$site_4_2.pNo45.t2" "PNotebook2_t3_5" vTcl:WidgetProc "Toplevel1" 1
    $site_4_2.pNo45 add $site_4_2.pNo45.t2 \
        -padding 0 -sticky nsew -state normal -text {ICMP Flood} -image {} \
        -compound none -underline -1 
    set site_6_1  $site_4_2.pNo45.t2
    frame $site_4_2.pNo45.t1 \
        -relief raised -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$site_4_2.pNo45.t1" "PNotebook2_t2_6" vTcl:WidgetProc "Toplevel1" 1
    $site_4_2.pNo45 add $site_4_2.pNo45.t1 \
        -padding 0 -sticky nsew -state normal -text {HTTP Flood} \
        -image image2 -compound none -underline -1 
    set site_6_2  $site_4_2.pNo45.t1
    frame $site_4_2.pNo45.t3 \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$site_4_2.pNo45.t3" "PNotebook2_t4_7" vTcl:WidgetProc "Toplevel1" 1
    $site_4_2.pNo45 add $site_4_2.pNo45.t3 \
        -padding 0 -sticky nsew -state normal -text {UDP Flood} -image {} \
        -compound none -underline -1 
    set site_6_3  $site_4_2.pNo45.t3
    frame $site_4_2.pNo45.t4 \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$site_4_2.pNo45.t4" "PNotebook2_t5_8" vTcl:WidgetProc "Toplevel1" 1
    $site_4_2.pNo45 add $site_4_2.pNo45.t4 \
        -padding 0 -sticky nsew -state normal -text {IPSec Flood} -image {} \
        -compound none -underline -1 
    set site_6_4  $site_4_2.pNo45.t4
    frame $site_4_2.pNo45.t5 \
        -relief sunken -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$site_4_2.pNo45.t5" "PNotebook2_t6_9" vTcl:WidgetProc "Toplevel1" 1
    $site_4_2.pNo45 add $site_4_2.pNo45.t5 \
        -padding 0 -sticky nsew -state normal -text {IKE Flood} -image {} \
        -compound none -underline -1 
    set site_6_5  $site_4_2.pNo45.t5
    place $site_4_2.pNo45 \
        -in $site_4_2 -x 0 -relx 0.018 -y 0 -rely 0.041 -width 0 \
        -relwidth 0.964 -height 0 -relheight 0.918 -anchor nw \
        -bordermode ignore 
    frame $top.pNo47.t3 \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$top.pNo47.t3" "PNotebook1_t4_10" vTcl:WidgetProc "Toplevel1" 1
    $top.pNo47 add $top.pNo47.t3 \
        -padding 0 -sticky nsew -state normal -text Synflooder -image {} \
        -compound none -underline -1 
    set site_4_3  $top.pNo47.t3
    label $site_4_3.lab45 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Console Output} 
    vTcl:DefineAlias "$site_4_3.lab45" "Label6" vTcl:WidgetProc "Toplevel1" 1
    text $site_4_3.tex47 \
        -background white -font TkTextFont -foreground black -height 184 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 254 -wrap word 
    $site_4_3.tex47 configure -font "TkTextFont"
    $site_4_3.tex47 insert end text
    vTcl:DefineAlias "$site_4_3.tex47" "Text1" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_3.lab48 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Enter IP:} 
    vTcl:DefineAlias "$site_4_3.lab48" "Label7" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_3.lab49 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Target Port:} 
    vTcl:DefineAlias "$site_4_3.lab49" "Label8" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_3.lab52 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Packet Count:} 
    vTcl:DefineAlias "$site_4_3.lab52" "Label9" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_3.lab53 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Packet Size:} 
    vTcl:DefineAlias "$site_4_3.lab53" "Label10" vTcl:WidgetProc "Toplevel1" 1
    spinbox $site_4_3.spi54 \
        -activebackground #f9f9f9 -background white -buttonbackground #d9d9d9 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground black \
        -from 1.0 -highlightbackground black -highlightcolor black \
        -increment 1.0 -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable spinbox -to 100.0 -values 80 
    vTcl:DefineAlias "$site_4_3.spi54" "Spinbox1" vTcl:WidgetProc "Toplevel1" 1
    spinbox $site_4_3.spi55 \
        -activebackground #f9f9f9 -background white -buttonbackground #d9d9d9 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground black \
        -from 1.0 -highlightbackground black -highlightcolor black \
        -increment 1.0 -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable spinbox -to 100.0 
    vTcl:DefineAlias "$site_4_3.spi55" "Spinbox1_1" vTcl:WidgetProc "Toplevel1" 1
    spinbox $site_4_3.spi56 \
        -activebackground #f9f9f9 -background white -buttonbackground #d9d9d9 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground black \
        -from 1.0 -highlightbackground black -highlightcolor black \
        -increment 1.0 -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable spinbox -to 100.0 
    vTcl:DefineAlias "$site_4_3.spi56" "Spinbox1_2" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_3.lab57 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {dai dai} 
    vTcl:DefineAlias "$site_4_3.lab57" "Label11" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_3.but58 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Launch 
    vTcl:DefineAlias "$site_4_3.but58" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_3.but60 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Stop 
    vTcl:DefineAlias "$site_4_3.but60" "Button1_3" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_3.lab45 \
        -in $site_4_3 -x 0 -relx 0.518 -y 0 -width 0 -relwidth 0.195 \
        -height 0 -relheight 0.115 -anchor nw -bordermode ignore 
    place $site_4_3.tex47 \
        -in $site_4_3 -x 0 -relx 0.518 -y 0 -rely 0.119 -width 0 \
        -relwidth 0.454 -height 0 -relheight 0.811 -anchor nw \
        -bordermode ignore 
    place $site_4_3.lab48 \
        -in $site_4_3 -x 0 -relx 0.048 -y 0 -rely 0.031 -width 0 \
        -relwidth 0.111 -height 0 -relheight 0.159 -anchor nw \
        -bordermode ignore 
    place $site_4_3.lab49 \
        -in $site_4_3 -x 0 -y 0 -rely 0.22 -width 0 -relwidth 0.164 -height 0 \
        -relheight 0.115 -anchor nw -bordermode ignore 
    place $site_4_3.lab52 \
        -in $site_4_3 -x 0 -y 0 -rely 0.396 -width 0 -relwidth 0.17 -height 0 \
        -relheight 0.115 -anchor nw -bordermode ignore 
    place $site_4_3.lab53 \
        -in $site_4_3 -x 0 -relx 0.018 -y 0 -rely 0.573 -width 0 \
        -relwidth 0.146 -height 0 -relheight 0.115 -anchor nw \
        -bordermode ignore 
    place $site_4_3.spi54 \
        -in $site_4_3 -x 0 -relx 0.196 -y 0 -rely 0.22 -width 0 \
        -relwidth 0.154 -height 0 -relheight 0.106 -anchor nw \
        -bordermode ignore 
    place $site_4_3.spi55 \
        -in $site_4_3 -x 0 -relx 0.196 -y 0 -rely 0.396 -width 0 \
        -relwidth 0.154 -height 0 -relheight 0.106 -anchor nw \
        -bordermode ignore 
    place $site_4_3.spi56 \
        -in $site_4_3 -x 0 -relx 0.196 -y 0 -rely 0.573 -width 0 \
        -relwidth 0.154 -height 0 -relheight 0.106 -anchor nw \
        -bordermode ignore 
    place $site_4_3.lab57 \
        -in $site_4_3 -x 0 -relx 0.179 -y 0 -rely 0.044 -width 0 \
        -relwidth 0.075 -height 0 -relheight 0.115 -anchor nw \
        -bordermode ignore 
    place $site_4_3.but58 \
        -in $site_4_3 -x 0 -relx 0.054 -y 0 -rely 0.793 -width 96 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_3.but60 \
        -in $site_4_3 -x 0 -relx 0.268 -y 0 -rely 0.789 -width 96 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    ttk::style configure TFrame -background $vTcl(actual_gui_bg)
    ttk::frame $top.tFr47 \
        -borderwidth 2 -relief groove -width 315 -height 25 
    vTcl:DefineAlias "$top.tFr47" "TFrame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.tFr47
    ttk::label $site_3_0.tLa50 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left \
        -text {Tasks Running: 3  Flooder\synFlooder} 
    vTcl:DefineAlias "$site_3_0.tLa50" "TLabel1" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.tLa50 \
        -in $site_3_0 -x 0 -y 0 -width 0 -relwidth 0.859 -height 0 \
        -relheight 1.08 -anchor nw -bordermode ignore 
    ttk::style configure TFrame -background $vTcl(actual_gui_bg)
    ttk::frame $top.tFr48 \
        -borderwidth 2 -relief groove -width 295 -height 25 
    vTcl:DefineAlias "$top.tFr48" "TFrame1_1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.tFr48
    ttk::label $site_3_0.tLa51 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left \
        -text {UP: 20KB} 
    vTcl:DefineAlias "$site_3_0.tLa51" "TLabel2" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $site_3_0.tLa52 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left \
        -text {DWN: 500KB} 
    vTcl:DefineAlias "$site_3_0.tLa52" "TLabel3" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.tLa51 \
        -in $site_3_0 -x 0 -relx 0.237 -y 0 -width 0 -relwidth 0.322 \
        -height 0 -relheight 0.96 -anchor nw -bordermode ignore 
    place $site_3_0.tLa52 \
        -in $site_3_0 -x 0 -relx 0.576 -y 0 -width 0 -relwidth 0.39 -height 0 \
        -relheight 0.96 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra45 \
        -in $top -x 0 -relx 0.017 -y 0 -rely 0.025 -width 0 -relwidth 0.959 \
        -height 0 -relheight 0.168 -anchor nw -bordermode ignore 
    place $top.pNo47 \
        -in $top -x 0 -relx 0.033 -y 0 -rely 0.212 -width 0 -relwidth 0.934 \
        -height 0 -relheight 0.689 -anchor nw -bordermode ignore 
    place $top.tFr47 \
        -in $top -x 0 -y 0 -rely 0.94 -width 0 -relwidth 0.522 -height 0 \
        -relheight 0.063 -anchor nw -bordermode ignore 
    place $top.tFr48 \
        -in $top -x 0 -relx 0.513 -y 0 -rely 0.94 -width 0 -relwidth 0.488 \
        -height 0 -relheight 0.063 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
