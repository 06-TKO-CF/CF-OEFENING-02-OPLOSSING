import FreeSimpleGUI as sg

from . import init_layout
from .app_layout import appLayout

from entiteit.container import Container
from bin.imagetkhelper import ImageTKHelper

import os
import shutil

class App:
    def __init__(self):
        self._container = Container()
        self._oBloem = None
        self._mode = 'NIEUW'

    def toon(self):
        self._venster = sg.Window(
            title = '',
            layout = appLayout(),
            resizable = False,
            finalize = True
        )

        self._selecteer()
        self._update()

        while True:
            evt, vals = self._venster.read()

            match evt:
                case sg.WIN_CLOSED | '-BTN-AFSLUITEN-':
                    break

                case '-BTN-FOTO-':
                    self._uploadFoto()  

                case '-LBX-OVERZICHT-':
                    if len(vals['-LBX-OVERZICHT-']) > 0:
                        self._oBloem = vals['-LBX-OVERZICHT-'][0]
                        self._mode = 'BEWERK'
                        self._update()

                case '-BTN-NIEUW-':
                    self._mode = 'BEWAAR'
                    self._oBloem = self._container.nieuw()
                    self._update()

                case '-BTN-BEWERK-':
                    self._mode = 'BEWAAR'
                    self._update()

                case '-BTN-VERWIJDER-':
                    self._verwijder()

                case '-BTN-BEWAAR-':
                    self._bewaar(vals)

                case '-BTN-ANNULEER-':
                    self._selecteer()

        self._venster.close()
        
    def _selecteer(self):
        lijst = self._container.lijst()

        self._venster['-LBX-OVERZICHT-'].update(disabled = False)
        self._venster['-LBX-OVERZICHT-'].update(values=lijst)

        if len(lijst) > 0:
            self._oBloem = lijst[0]
            self._venster['-LBX-OVERZICHT-'].update(set_to_index = 0)
            self._mode = 'BEWERK'
        else:
            self._oBloem = self._container.nieuw()
            self._mode = 'NIEUW'
        self._update()

    def _update(self):
        if self._oBloem:            
            self._venster['-INP-NAAM-'].update(value=self._oBloem.naam)
            self._venster['-INP-BESCHRIJVING-'].update(value=self._oBloem.beschrijving)
            self._venster['-INP-FOTO-'].update(value=self._oBloem.foto)

            if os.path.exists(self._oBloem.foto):
                self._venster['-IMG-FOTO-'].update(data=ImageTKHelper.passend(pad=self._oBloem.foto, grootte=(200, 200)))
            else:
                self._venster['-IMG-FOTO-'].update(data=ImageTKHelper.passend(pad='assets/fotoPlaatshouder.jpg', grootte=(200, 200)))

        self._venster['-INP-NAAM-'].update(readonly = self._mode != 'BEWAAR')
        self._venster['-INP-BESCHRIJVING-'].update(readonly = self._mode != 'BEWAAR')
        self._venster['-BTN-FOTO-'].update(visible = self._mode == 'BEWAAR')
        self._venster['-LBX-OVERZICHT-'].update(disabled = self._mode == 'BEWAAR')
        self._venster['-BTN-BEWAAR-'].update(visible = self._mode == 'BEWAAR')
        self._venster['-BTN-ANNULEER-'].update(visible = self._mode == 'BEWAAR')
        # self._venster['-BTN-NIEUW-'].update(visible = (self._mode == 'NIEUW') or (self._mode == 'BEWERK'))
        self._venster['-BTN-NIEUW-'].update(disabled = (self._mode != 'NIEUW') and (self._mode != 'BEWERK'))
        self._venster['-BTN-BEWERK-'].update(visible = self._mode == 'BEWERK')
        self._venster['-BTN-VERWIJDER-'].update(visible = self._mode == 'BEWERK')

    def _uploadFoto(self):
        pad = sg.popup_get_file(
            title = 'Selecteer foto',
            message = 'Selecteer foto bloem',
            multiple_files = False,
            file_types = (('JPEG', '.jpg'), ('PNG', '.png'))
        )

        if pad:
            try:
                bestandNaam, bestandExt = os.path.splitext(pad)
                padFoto = self._oBloem.padFotoNieuw(bestandExt)
                shutil.copy(pad, padFoto, follow_symlinks=True)
                self._venster['-INP-FOTO-'].update(value=padFoto)
                self._oBloem.foto = padFoto
                self._venster['-IMG-FOTO-'].update(data=ImageTKHelper.passend(pad=padFoto, grootte=(200, 200)))
            except Exception as ex:
                sg.popup_error('Fout bij uploaden afbeelding', 'FOUT uploaden !')
    
    def _verwijder(self):
        try:
            self._container.verwijder(self._oBloem)
            self._selecteer()
        except Exception as ex:
            sg.popup_error(ex, title='FOUT')

    def _bewaar(self, vals):
        try:
            naam = vals['-INP-NAAM-']
            beschrijving = vals['-INP-BESCHRIJVING-']
            foto = vals['-INP-FOTO-']
            self._container.update(self._oBloem, naam, beschrijving, foto)
            self._selecteer()
        except Exception as ex:
            sg.popup_error(ex, title='FOUT')
        
