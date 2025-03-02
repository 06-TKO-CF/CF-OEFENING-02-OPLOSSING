import FreeSimpleGUI as sg

kolomLinks = sg.Column(
    expand_y = True,
    layout = [
        [
            sg.Frame(
                title = 'Detail',
                expand_y = True,
                layout = [
                    [
                        sg.Text(
                            text = 'naam'
                        )
                    ],
                    [
                        sg.Input(
                            default_text = '',
                            readonly = True,
                            pad = ((40,20),(0,10)),
                            key = '-INP-NAAM-'
                        )
                    ],
                    [
                        sg.Text(
                            text = 'beschrijving'
                        )
                    ],
                    [
                        sg.Input(
                            default_text = '',
                            readonly = True,
                            pad = ((40,20),(0,10)),
                            key = '-INP-BESCHRIJVING-'
                        )
                    ],
                    [
                        sg.Text(
                            text = 'foto'
                        ),
                        sg.Input(
                            default_text = '',
                            visible = False,
                            key = '-INP-FOTO-'
                        ),
                        sg.Push(),
                        sg.Button(
                            button_text = 'foto uploaden',
                            key = '-BTN-FOTO-',
                            pad = ((0,10), (0,0)),
                            # visible = False
                        )
                    ],
                    [
                        sg.Image(
                            pad = ((40,20),(10,10)),
                            key = '-IMG-FOTO-',
                            size = (200, 200)
                        )
                    ],
                    [
                        sg.VPush()
                    ],
                    [
                        sg.HorizontalSeparator(
                            pad = (0, 10)
                        )
                    ],
                    [
                        sg.Button(
                            button_text = 'Nieuw',
                            size = (10,1),
                            key = '-BTN-NIEUW-',
                            pad = ((0,10), (0,10))
                        ),
                        sg.Push(),
                        sg.Button(
                            button_text = 'Verwijder',
                            size = (10,1),
                            key = '-BTN-VERWIJDER-',
                            visible = False,
                            pad = ((0,10), (0,10))
                        ),
                        sg.Button(
                            button_text = 'Bewerk',
                            size = (10,1),
                            key = '-BTN-BEWERK-',
                            visible = False,
                            pad = ((0,10), (0,10))
                        ),
                        sg.Button(
                            button_text = 'Bewaar',
                            size = (10,1),
                            key = '-BTN-BEWAAR-',
                            visible = False,
                            pad = ((0,10), (0,10))
                        ),
                        sg.Button(
                            button_text = 'Annuleer',
                            size = (10,1),
                            key = '-BTN-ANNULEER-',
                            visible = False,
                            pad = ((0,10), (0,10))
                        ),
                    ]
                ]
            )
        ]
    ]
)

kolomRechts = sg.Column(
    layout = [
        [
            sg.Frame(
                title = 'Lijst',
                layout = [
                    [
                        sg.Listbox(
                            values = [],
                            key = '-LBX-OVERZICHT-',
                            enable_events = True,
                            select_mode = sg.LISTBOX_SELECT_MODE_SINGLE,
                            size = (40, 20),
                            pad = (15, 15)
                        )
                    ]
                ]
            )
        ]
    ]
)

def appLayout():
    return [
        [
            sg.Push(),
            sg.Image(
                source = 'assets/logo.png'
            ),
            sg.Text(
                text = 'Bloemen',
                font = ('Calibri', 24)
            ),
            sg.Push()
        ],
        [
            sg.HorizontalSeparator(
                pad = (0, 15)
            )
        ],
        [
            kolomLinks,
            kolomRechts
        ],
        
        [
            sg.HorizontalSeparator(
                pad = (0, 15)
            )
        ],
        [
            sg.Push(),
            sg.Button(
                button_text = 'Afsluiten',
                key = '-BTN-AFSLUITEN-',
                size = (10, 1)
            )
        ]
    ]