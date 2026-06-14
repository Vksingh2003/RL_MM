# GTFA Angela Brooks Portfolio Review

## Persona

Angela Brooks

## Category

Creative & Media

## Subcategory

Design/Portfolio Review

## Folder Name

vivekkumarsingh_Angela_Brooks

## User Prompt

I need a portfolio review CSV with one row per design piece and a final status for each row.
Use the latest approval record and the actual design files to decide each status while keeping every piece mapped to its original project category.
Return the final CSV with statuses Ready, Revise, or Exclude.

## Expected Final Output

The final answer must be a CSV file with one row per design piece.

The CSV must use these columns:

```csv
item_id,design_piece,project_category,approval_source,design_file,final_status
```

## Expected CSV

```csv
item_id,design_piece,project_category,approval_source,design_file,final_status
DES-001,Greenleaf Donation Page Redesign,Freelance Client,Latest_Approval_Record.csv,Greenleaf_Donation_Page_Final.png,Ready
DES-002,Harborview Booking Flow Redesign,Freelance Client,Latest_Approval_Record.csv,Harborview_Booking_Flow_Final.pdf,Ready
DES-003,Briarwood Parent Onboarding Flow,Freelance Client,Latest_Approval_Record.csv,Briarwood_Onboarding_Design_Export_DES003.png,Revise
DES-004,CID Interaction Design Capstone Board,School Work,Latest_Approval_Record.csv,CID_Capstone_Board_Final.pdf,Ready
DES-005,Portfolio Homepage Case Study Tile,Portfolio Work,Latest_Approval_Record.csv,Portfolio_Homepage_Tile_Final.png,Ready
DES-006,Lantern Tides Pier Scene,Lantern Tides,Latest_Approval_Record.csv,Lantern_Tides_Clearance_Board_DES006.png,Exclude
DES-007,Lantern Tides Dialogue UI Mockup,Lantern Tides,Latest_Approval_Record.csv,Lantern_Tides_Dialogue_UI_Final.png,Ready
DES-008,Briarwood Tutor Match Screen,Freelance Client,Latest_Approval_Record.csv,Briarwood_Tutor_Match_Final.png,Ready
```

## Ground Truth Facts

1. The final output must be a CSV.
2. The CSV must contain one row per design piece.
3. The CSV must include item_id design_piece project_category approval_source design_file final_status.
4. The only valid final_status values are Ready Revise Exclude.
5. The latest approval record is the authority for status decisions.
6. Actual design files must be checked before assigning final_status.
7. Each design piece must stay mapped to its original project category.
8. Freelance Client items must stay separate from School Work.
9. Lantern Tides items must stay separate from client work.
10. Portfolio Work items must stay separate from client and school work.
11. Older approval records must not override Latest_Approval_Record.csv.
12. Older portfolio trackers must not override the current item tracker.
13. Archived portfolio guidelines must not override current portfolio rules.
14. Wrong-client design files must not appear in the final CSV.
15. Duplicate design file records must not create duplicate output rows.
16. Draft approval records must not be treated as latest approval.
17. Unapproved Lantern Tides concepts must not be included as Ready.
18. Lantern Tides materials marked internal only must be Exclude.
19. DES-003 must be Revise because the current design file contains a revision issue.
20. DES-006 must be Exclude because the current Lantern Tides clearance board marks it internal only.
21. Noise files must not affect final statuses.
22. The answer must not create new design pieces.
23. The answer must not invent extra statuses.
24. The answer must not return a narrative instead of the CSV.

## Required Source Joins

1. Join portfolio item records to latest approval records using item_id.
2. Join actual design files to portfolio item records using item_id.
3. Join each item to its original project category using the category mapping source.
4. Reconcile design-file evidence against the latest approval record before assigning status.
5. Use current design evidence to catch revision or exclusion cases that approval text alone does not fully resolve.

## Expected Status Logic

1. Ready means the design piece is current approved and visually acceptable for the review set.
2. Revise means the design piece is approved for consideration but the actual design file shows a fix required.
3. Exclude means the design piece is not approved for the review set or belongs to material that must not be shared.

## Trap Handling

1. Temporal Revision: Use the latest approval record instead of old approval records or archived guidelines.
2. Cross-Modal Contradiction: If a text record says an item is usable but the actual design file shows a revision or clearance problem then the visual evidence must affect the status.
3. Wrong Source Trap: Do not include wrong-client assets in the final CSV.
4. Distractor Noise: Ignore unrelated files such as Makerspace notes boba references DND notes trip moodboards and invoice logs.
5. Duplicate Trap: Do not create duplicate output rows from duplicate design indexes.
6. Privacy Boundary Trap: Keep Lantern Tides materials separate and exclude any internal-only or unapproved game asset.

## Hard Fail Conditions

1. The response omits the CSV.
2. The response omits any required column.
3. The response uses a status other than Ready Revise Exclude.
4. The response marks DES-003 as Ready.
5. The response marks DES-006 as Ready or Revise.
6. The response includes wrong-client assets.
7. The response uses archived guidelines as the final authority.
8. The response uses draft approvals as the final authority.
9. The response mixes project categories.
10. The response duplicates design pieces.
11. The response includes noise files as portfolio items.
12. The response writes a general summary instead of the final CSV.

## Notes for Rubric Alignment

The rubric should reward correct CSV output correct status labels correct item-category mapping correct use of latest approval evidence correct visual file inspection and correct exclusion of stale wrong-client duplicate and noise records.

The rubric should include negative criteria for using stale drafts creating new design pieces and including wrong-client or internal-only assets.
