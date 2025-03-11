from django.urls import path
from . import views
from .views import convert_file ,sdf_smi , sdf_to_smi ,smi_pdb , smi_to_pdb , pdb_smi, mol2_sdf , mol2_to_sdf ,pdb_to_mol2, pdb_mol2, mol2_pdb , mol2_to_pdb
from .views import pdb_to_smi,sdf_pdb, sdf_to_pdb ,pdb_sdf, pdb_to_sdf , smi_to_mol2 , smi_mol2 , mol2_to_smi, mol2_smi , sdf_to_mol2 , sdf_mol2

urlpatterns = [
    path('', views.index, name="index"),
    path('convert/', views.convert_file, name='convert_file'),
    path('split/', views.split, name="split"),
    path('conversion', views.conversion, name='conversion'), 
    path('convert/', convert_file, name='convert_file'),

    path('sdf-to-smi/', sdf_to_smi, name='sdf_to_smi'),
    path('sdf-smi/', sdf_smi, name='sdf_smi'), 

    path('smi-to-pdb/',smi_to_pdb, name='smi_to_pdb'),
    path('smi-pdb/',smi_pdb, name='smi_pdb'),

    path('pdb-to-smi/',pdb_to_smi, name='pdb_to_smi'),
    path('pdb-smi/',pdb_smi, name='pdb_smi'),

    path('sdf-to-pdb/',sdf_to_pdb, name='sdf_to_pdb'),
    path('sdf-pdb/',sdf_pdb, name='sdf_pdb'),

    path('pdb-to-sdf/',pdb_to_sdf, name='pdb_to_sdf'),
    path('pdb-sdf/',pdb_sdf, name='pdb_sdf'),

    path('smi-to-mol2/',smi_to_mol2, name='smi_to_mol2'),
    path('smi-mol2/',smi_mol2, name='smi_mol2'),

    path('mol2-to-smi/',mol2_to_smi, name='mol2_to_smi'),
    path('mol2-smi/',mol2_smi, name='mol2_smi'),

    path('sdf-to-mol2/',sdf_to_mol2, name='sdf_to_mol2'),
    path('sdf-mol2/',sdf_mol2, name='sdf_mol2'),

    path('mol2-to-sdf/',mol2_to_sdf, name='mol2_to_sdf'),
    path('mol2-sdf/',mol2_sdf, name='mol2_sdf'),

    path('pdb-to-mol2/',pdb_to_mol2, name='pdb_to_mol2'),
    path('pdb-mol2/',pdb_mol2, name='pdb_mol2'),

    path('mol2-to-pdb/',mol2_to_pdb, name='mol2_to_pdb'),
    path('mol2_pdb/', views.mol2_pdb, name='mol2_pdb'),





]
