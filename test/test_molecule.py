
from qmworks import rdkitTools
from qmworks import packages


def test_SerMolecule():
    mol = rdkitTools.smiles2plams("c1ccccc1CC")
    registry = packages.registry()
    encoded_molecule = registry.deep_encode(mol)
    decoded_molecule = registry.deep_decode(encoded_molecule)
    assert len(mol) == len(decoded_molecule)
