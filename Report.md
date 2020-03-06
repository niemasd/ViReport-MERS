# ViReport v0.0.1 &mdash; 2020-03-06

## Input Dataset
The analysis was conducted on a dataset containing 274 sequences.
The average sequence length was 30130,
with a standard deviation of 0.
The earliest sample date was 2012-04-15,
the median sample date was 2014-11-01,
and the most recent sample date was 2015-09-17.


<figure>
<img src="./report_files/figs/input_sequence_lengths.png" width="auto" height="auto" style="max-width:75%;">
<figcaption>Distribution of input sequence lengths</figcaption>
</figure>



<figure>
<img src="./report_files/figs/input_sample_dates.png" width="auto" height="auto" style="max-width:75%;">
<figcaption>Distribution of input sample dates</figcaption>
</figure>


## Preprocessed Dataset
The input dataset was preprocessed such that sequences were given safe names: non-letters/digits in sequence IDs were converted to underscores.
After preprocessing, the dataset contained 274 sequences.
The average sequence length was 30130,
with a standard deviation of 0.
The earliest sample date was 2012-04-15,
the median sample date was 2014-11-01,
and the most recent sample date was 2015-09-17.


<figure>
<img src="./report_files/figs/processed_sequence_lengths.png" width="auto" height="auto" style="max-width:75%;">
<figcaption>Distribution of preprocessed sequence lengths</figcaption>
</figure>



<figure>
<img src="./report_files/figs/processed_sample_dates.png" width="auto" height="auto" style="max-width:75%;">
<figcaption>Distribution of preprocessed sample dates</figcaption>
</figure>


## Multiple Sequence Alignment
Multiple sequence alignment was performed using MAFFT (Katoh & Standley, 2013) in automatic mode.
There were 31015 positions (16180 invariant) and 165 unique sequences in the multiple sequence alignment.
Pairwise distances were computed from the multiple sequence alignment using the tn93 tool of HIV-TRACE (Pond et al., 2018).
The average pairwise sequence distance was 0.0020438096315726533,
with a standard deviation of 0.0008959792782581416.


<figure>
<img src="./report_files/figs/pairwise_distances_sequences.png" width="auto" height="auto" style="max-width:75%;">
<figcaption>Distribution of pairwise sequence distances</figcaption>
</figure>


## Phylogenetic Inference
A maximum-likelihood phylogeny was inferred using IQ-TREE (Nguyen et al., 2015) in ModelFinder Plus mode (Kalyaanamoorthy et al., 2017).
The inferred phylogeny was MinVar-rooted using FastRoot (Mai et al., 2017).
Pairwise distances were computed from the phylogeny using TreeSwift (Moshiri, 2020).
The maximum pairwise phylogenetic distance (i.e., tree diameter) was 0.008118329899999999,
and the average pairwise phylogenetic distance was 0.0028314104874094747,
with a standard deviation of 0.0014109307953619646.


<figure>
<img src="./report_files/figs/tree_mutations.png" width="auto" height="auto" style="max-width:100%;max-height:100%;">
<figcaption>Rooted phylogenetic tree in unit of expected per-site mutations</figcaption>
</figure>



<figure>
<img src="./report_files/figs/pairwise_distances_tree.png" width="auto" height="auto" style="max-width:75%;">
<figcaption>Distribution of pairwise phylogenetic distances</figcaption>
</figure>


## Phylogenetic Dating
The rooted phylogeny was dated using treedater (Volz & Frost, 2017).
The height of the dated tree was 3.9417811427742464 days,
so given that the most recent sample was collected on 2015-09-17,
the estimated time of the most recent common ancestor (tMRCA) was 2015-09-13.


<figure>
<img src="./report_files/figs/tree_time.png" width="auto" height="auto" style="max-width:100%;max-height:100%;">
<figcaption>Dated phylogenetic tree in unit of years</figcaption>
</figure>


## Transmission Clustering
Transmission clustering was performed using TreeN93 (Moshiri, 2018) using pairwise phylogenetic distances.
The total number of singletons (i.e., non-clustered individuals) was 79,
and the total number of clusters (excluding singletons) was 25.
The average cluster size (excluding singletons) was 3.8,
with a standard deviation of 3.0724582991474434,
and the maximum and minimum cluster sizes were 16 and 2, respectively.


<figure>
<img src="./report_files/figs/cluster_sizes.png" width="auto" height="auto" style="max-width:75%;">
<figcaption>Distribution of cluster sizes (excluding singletons)</figcaption>
</figure>

