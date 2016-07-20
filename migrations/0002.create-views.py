#
#  file: migrations/0002.create-views.py
#
from yoyo import step
#
steps = [
#     step("""CREATE VIEW run_info AS
#             SELECT p.pipelinename, p.counter, p.triggermessage, s.approvedby, s.stageindex, s.result, s.scheduleddate, a.agentname
#             FROM pipeline p
#             JOIN stage s
#             ON s.pipelinecounter = p.counter AND s.pipelinename = p.pipelinename
#             JOIN agent a
#             ON s.agentuuid = a.id
#             WHERE s.result <> 'Cancelled'
#             ORDER BY p.counter DESC, s.stageindex DESC;""",
#          "DROP VIEW run_info;"),
#
    step("""CREATE VIEW failure_info AS
            SELECT p.pipeline_name, p.pipelinecounter, s.stage_counter, s.id, s.name as stage_name, p.triggermessage, s.approvedby, s.result, f.failurestage, s.scheduled_date
            FROM pipeline_instance p
            JOIN stage s ON s.instance_id = p.id
            LEFT JOIN failureinformation f ON f.stageid = s.id
            WHERE s.result <> 'Cancelled'
            ORDER BY p.pipelinecounter DESC, s.stage_counter DESC;""",
         "DROP VIEW failure_info;"),
#
#     step("""CREATE VIEW texttest_failures AS
#             SELECT p.pipelinename, p.counter, p.triggermessage, s.approvedby, s.stageindex, t.testindex, t.failuretype, t.documentname
#             FROM pipeline p
#             JOIN stage s ON s.pipelinecounter = p.counter AND s.pipelinename = p.pipelinename
#             JOIN texttestfailure t ON t.stageid = s.id
#             ORDER BY p.counter DESC, s.stageindex DESC, t.testindex ASC, t.documentname ASC;""",
#          "DROP VIEW texttest_failures;"),
#
#     step("""CREATE VIEW all_data AS
#             SELECT p.pipelinename, p.counter, p.triggermessage, s.approvedby, s.stageindex, s.result, s.scheduleddate, a.agentname, f.failurestage, t.testindex, t.failuretype, t.documentname
#             FROM pipeline p
#             JOIN stage s
#             ON s.pipelinecounter = p.counter AND s.pipelinename = p.pipelinename
#             JOIN agent a
#             ON s.agentuuid = a.id
#             FULL OUTER JOIN texttestfailure t ON t.stageid = s.id
#             FULL OUTER JOIN failureinformation f ON f.stageid = s.id
#             WHERE s.result <> 'Cancelled'
#             ORDER BY p.counter DESC, s.stageindex DESC, t.testindex ASC, t.documentname ASC;""",
#          "DROP VIEW all_data;")
]
