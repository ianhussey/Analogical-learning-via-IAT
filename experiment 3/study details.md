# The IAT as an analogical learning task III - novel attitudes towards known stimuli  

## Experiment 3: the analogical nature of the effect 

Previous experiments demonstrated that the IAT functions as an analogical learning task as well as its traditional employment as a testing task. These experiments demonstrated the acquisition of attitudes towards previously unknown stimuli (Chinese characters) in both local and online presentation formats. The current experiment seeks to replicate and extend these results, and explore whether the evaluative learning via the IAT is influenced by the strength and salience of the analogy present in the IAT. This study therefore seeks to provide more direct evidence that the observed learning effect observed in previous studies is analogical (as opposed to a more general contrast effect or other non-analogical explanations).

## Design

Between groups design

### IV

- Training IAT 
  - 2 (IAT contrast category condition) X 2 (attribute category condition)
    - flowers-chinese with oppositely valenced attributes
    - flowers-chinese with nonword attributes
    - insects-chinese with oppositely valenced attributes
    - insects-chinese with nonword attributes

### DVs

- Chinese self-report ratings
- Chinese SC-IAT
- Relational matching to sample task

### Counterbalancing

- Block order (identical for IAT & SCIAT)

## Measures

1. Demographics
2. IAT
3. Evaluative tasks
   - SC-IAT
   - Ratings

## Hypotheses

H1: IAT condition affects SCIAT effects in the oppositely valenced attributes IATs [conceptual replication of previous studies].

H2: Interaction between IAT condition and attribute condition affects SCIAT effects [extension].

H3: IAT condition affects ratings in the oppositely valenced attributes IATs [conceptual replication of previous studies].

H4: Interaction between IAT condition and attribute condition affects ratings [extension].

## Sample

Recruit online via prolific

### Planned sample size

Traditional power analysis is difficult given use of linear mixed effects models. To be frank, I don't have the skills to run simulations for this yet. Large sample size was chosen in the absense of power analysis.

Two groups planned plus headroom for some exclusions. Planned N = 440.

### Payment

£0.90 per participant (9 mins)

## Analytic strategy

### Exclusion criteria

Incomplete data.

Participants who have >10% of RTs < 300ms on the IAT's test blocks (3, 4, 6, 7) will be excluded from the analysis. NB the accuracy criterion is applied to the IAT on the expecation that the nonwords as attributes IAT may be difficult for participants. As a negative control condition, low accuracy rates on this task would not be problematic for the hypothesis being tested. This criterion is therefore removed for this study (cf the previous study).

Participants who have >10% of RTs < 300ms on the SCIAT test blocks (2 and 3) will be excluded from the analysis.

This provides a way to screen for low quality responding given the internet based sample.

### Data reduction

For the mixed models, reaction times will be subjected to a reciprocal transformation (1000/rt = rate, or keypresses per second) to reduce skew. RTs < 300ms will be trimmed before applying the transformation.

### Analyses 

#### Mixed models

Mixed models integrate both scoring and analysis and therefore minimise information loss, thereby providing greater power. Given that the effects observed in this study might be relativley small, we prespecify the used of mixed models. The specific models below accomplish the same goals as D1 scoring, i.e., by controlling for general responding speed and differences in the SC-IAT effect between participants. 

H1: 

- linear model: recip_rt ~ SCIAT_block *  IAT_condition + (SCIAT_block | participant)

H2: 

- linear model: recip_rt ~ SCIAT_block *  IAT_condition * attribute_condition + (SCIAT_block | participant)

H3: 

- linear model: rating ~  IAT_condition + (1 | participant)

H4: 

- linear model: rating ~  IAT_condition * attribute_condition + (1 | participant)

