__author__ = 'mnowotka'

#-----------------------------------------------------------------------------------------------------------------------

from rdkit import Chem
from chembl_beaker.beaker.utils.functional import _apply
from chembl_beaker.beaker.utils.io import _parseMolData, _parseSMILESData, _getSMILESString, _getSDFString
from chembl_beaker.beaker.utils.chemical_transformation import _computeCoords

#-----------------------------------------------------------------------------------------------------------------------

def _canonicalize_smiles(data, computeCoords=False, in_delimiter=' ', smilesColumn=0, nameColumn=1, titleLine=True,
    sanitize=True, out_delimiter=' ', nameHeader='Name', includeHeader=True, isomericSmiles=False, kekuleSmiles=False):
    return _getSMILESString(_parseSMILESData(data, computeCoords=computeCoords, delimiter=in_delimiter,
        smilesColumn=smilesColumn, nameColumn=nameColumn, titleLine=titleLine, sanitize=sanitize),
        delimiter=out_delimiter, nameHeader=nameHeader, includeHeader=includeHeader, isomericSmiles=isomericSmiles,
                     kekuleSmiles=kekuleSmiles)

#-----------------------------------------------------------------------------------------------------------------------

def _ctab2smiles(data, sanitize=True, removeHs=True, strictParsing=True, delimiter=' ', nameHeader='Name',
                 includeHeader=True, isomericSmiles=False, kekuleSmiles=False):
    return _getSMILESString(_parseMolData(data, sanitize=sanitize, removeHs=removeHs, strictParsing=strictParsing),
        delimiter=delimiter, nameHeader=nameHeader, includeHeader=includeHeader, isomericSmiles=isomericSmiles,
                     kekuleSmiles=kekuleSmiles)

#-----------------------------------------------------------------------------------------------------------------------

def _smiles2ctab(data, computeCoords=False, delimiter=' ', smilesColumn=0, nameColumn=1, titleLine=True, sanitize=True):
    return _getSDFString(_parseSMILESData(data, computeCoords=computeCoords, delimiter=delimiter,
        smilesColumn=smilesColumn, nameColumn=nameColumn, titleLine=titleLine, sanitize=sanitize))

#-----------------------------------------------------------------------------------------------------------------------

def _inchi2ctab(inchis):
    mols = _apply(inchis.split(),Chem.MolFromInchi)
    _apply(mols, _computeCoords)
    return _getSDFString(mols)

#-----------------------------------------------------------------------------------------------------------------------

def _ctab2inchi(data, sanitize=True, removeHs=True, strictParsing=True):
    return '\n'.join(_apply(_parseMolData(data, sanitize=sanitize, removeHs=removeHs, strictParsing=strictParsing),
        Chem.MolToInchi))

#-----------------------------------------------------------------------------------------------------------------------

def _inchi2inchiKey(inchis):
    return '\n'.join([Chem.InchiToInchiKey(inch) for inch in inchis.split()])

#-----------------------------------------------------------------------------------------------------------------------
