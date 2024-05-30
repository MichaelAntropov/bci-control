


select
    cast(sum(json_extract(process_results.results, '$.total_correct_itcca')) as double)/cast(sum(json_extract(process_results.results, '$.total_trials_tested')) as double) as itcca_accuracy
    ,cast(sum(json_extract(process_results.results, '$.total_correct_mix')) as double)/cast(sum(json_extract(process_results.results, '$.total_trials_tested')) as double) as mix_accuracy
    ,cast(sum(json_extract(process_results.results, '$.total_correct')) as double)/cast(sum(json_extract(process_results.results, '$.total_trials_tested')) as double) as cca_accuracy
from process_results
where parameters_id = :processs_param_id;





select cast(sum(json_extract(process_results.results, '$.total_correct_itcca')) as double)/cast(sum(json_extract(process_results.results, '$.total_trials_tested')) as double) as itcca_accuracy,
       cast(sum(json_extract(process_results.results, '$.total_correct_mix')) as double)/cast(sum(json_extract(process_results.results, '$.total_trials_tested')) as double) as mix_accuracy,
       cast(sum(json_extract(process_results.results, '$.total_correct')) as double)/cast(sum(json_extract(process_results.results, '$.total_trials_tested')) as double) as cca_accuracy
from process_results
join recordings
    on process_results.recording_id = recordings.id
where
    parameters_id = :processs_param_id and subject_id in :subject_id;


select * from process_results where json_extract(results, '$.accuracy') = 1;


select
    cast(sum(json_extract(pr.results, '$.total_correct_mix')) as double)/cast(sum(json_extract(pr.results, '$.total_trials_tested')) as double) as mix_accuracy
from process_results pr
join process_parameters pp
    on pr.parameters_id = pp.id
where parameters_id = 35;