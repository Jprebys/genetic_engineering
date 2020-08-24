# Data Description

This dataset consists of DNA sequences from genetically engineered plasmids. Plasmids are small, circular DNA molecules that replicate independently from chromosomes.

There are 41 columns in this dataset. Each row corresponds to a plasmid DNA sequence, which is uniquely identified by sequence_id, a 5-character alphanumeric string. In addition to the DNA sequences provided in sequence, there are 39 binary features that provide metadata about the plasmids. All variables are described below.

- `sequence` (type: string): A plasmid DNA sequence. Any Us were changed to Ts and letters other than A, T, G, C, or N were changed to Ns. Possible values: A, T, G, C, or N

- `bacterial_resistance_ampicillin`, `bacterial_resistance_chloramphenicol`, `bacterial_resistance_kanamycin`, `bacterial_resistance_other`, `bacterial_resistance_spectinomycin` (type: binary): One-hot encoded columns that indicate the antibiotic resistance of the plasmid used f`or selecting during bacterial growth and cloning.
- `copy_number_high_copy`, `copy_number_low_copy`, `copy_number_unknown` (type: binary): One-hot encoded columns that indicate the number of plasmids per bacterial cell.
- `growth_strain_ccdb_survival`, `growth_strain_dh10b`, `growth_strain_dh5alpha`, `growth_strain_neb_stable`, `growth_strain_other`, `growth_strain_stbl3`,`growth_strain_top10`, `growth_strain_xl1_blue` (type: binary): One-hot encoded columns that indicate the strain used to clone the plasmid.
- `growth_temp_30`, `growth_temp_37`, `growth_temp_other` (type: binary): One-hot encoded columns that indicate the temperature the plasmid should be grown at.
- `selectable_markers_blasticidin`, `selectable_markers_his3`, `selectable_markers_hygromycin`, `selectable_markers_leu2`, `selectable_markers_neomycin`, `selectable_markers_other`,`selectable_markers_puromycin`, `selectable_markers_trp1`, `selectable_markers_ura3`, `selectable_markers_zeocin` (type: binary): One-hot encoded columns that indicate genes that allow non-bacterial selection (for a plasmid used outside of the cloning organism).
- `species_budding_yeast`, `species_fly`, `species_human`, `species_mouse`,`species_mustard_weed`, `species_nematode`, `species_other`, `species_rat`, `species_synthetic`, `species_zebrafish` (type: binary): One-hot encoded columns that indicate the species the plasmid is used in, after cloning.
