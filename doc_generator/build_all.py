"""
Master Compiler: Converts all Phase HTML documents into high-resolution,
executive-grade PDFs via headless Microsoft Edge browser.
"""
import os
import subprocess
import time

from doc_generator.phase1 import (
    get_brainstorming_doc,
    get_problem_statements_doc,
    get_empathy_map_doc,
)
from doc_generator.phase2 import (
    get_customer_journey_doc,
    get_dfd_doc,
    get_solution_requirements_doc,
    get_tech_stack_doc,
)
from doc_generator.phase3 import (
    get_problem_solution_fit_doc,
    get_proposed_solution_doc,
    get_solution_architecture_doc,
)
from doc_generator.phase4 import (
    get_project_planning_doc,
)
from doc_generator.phase5 import (
    get_code_layout_doc,
    get_coding_solution_doc,
    get_functional_features_doc,
)
from doc_generator.phase6 import (
    get_performance_testing_doc,
)
from doc_generator.phase7 import (
    get_executable_files_doc,
    get_sample_documentation_doc,
)
from doc_generator.phase8 import (
    get_communication_doc,
    get_demo_features_doc,
    get_demo_planning_doc,
    get_scalability_doc,
    get_team_involvement_doc,
)

DOCUMENTS = [
    # Phase 1
    ("1. Brainstorming & Ideation", "Brainstorming & Idea Prioritization.pdf", get_brainstorming_doc),
    ("1. Brainstorming & Ideation", "Define Problem Statements.pdf", get_problem_statements_doc),
    ("1. Brainstorming & Ideation", "Empathy Map.pdf", get_empathy_map_doc),

    # Phase 2
    ("2. Requirement Analysis", "Customer Journey Map.pdf", get_customer_journey_doc),
    ("2. Requirement Analysis", "Data Flow Diagram.pdf", get_dfd_doc),
    ("2. Requirement Analysis", "Solution Requirements.pdf", get_solution_requirements_doc),
    ("2. Requirement Analysis", "Technology Stack.pdf", get_tech_stack_doc),

    # Phase 3
    ("3. Project Design Phase", "Problem-Solution Fit.pdf", get_problem_solution_fit_doc),
    ("3. Project Design Phase", "Proposed Solution.pdf", get_proposed_solution_doc),
    ("3. Project Design Phase", "Solution Architecture.pdf", get_solution_architecture_doc),

    # Phase 4
    ("4. Project Planning Phase", "Project Planning.pdf", get_project_planning_doc),

    # Phase 5
    ("5. Project Development Phase", "Code-Layout, Readability and Reusability.pdf", get_code_layout_doc),
    ("5. Project Development Phase", "Coding & Solution.pdf", get_coding_solution_doc),
    ("5. Project Development Phase", "No. of Functional Features Included in the Solution.pdf", get_functional_features_doc),

    # Phase 6
    ("6. Project Testing", "Performance Testing.pdf", get_performance_testing_doc),

    # Phase 7
    ("7. Project Documentation", "Project Executable Files.pdf", get_executable_files_doc),
    ("7. Project Documentation", "Sample Project Documentation.pdf", get_sample_documentation_doc),

    # Phase 8
    ("8. Project Demonstration", "Communication.pdf", get_communication_doc),
    ("8. Project Demonstration", "Demonstration of Proposed Features.pdf", get_demo_features_doc),
    ("8. Project Demonstration", "Project Demo Planning.pdf", get_demo_planning_doc),
    ("8. Project Demonstration", "Scalability & Future Plan.pdf", get_scalability_doc),
    ("8. Project Demonstration", "Team Involvement in Demonstration.pdf", get_team_involvement_doc),
]

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
BASE_DIR = r"C:\Travel-planner"
HTML_DIR = os.path.join(BASE_DIR, "docs_html")
DOCS_DIR = os.path.join(BASE_DIR, "docs")

def build_all_pdfs():
    os.makedirs(HTML_DIR, exist_ok=True)
    total = len(DOCUMENTS)
    print(f"Starting compilation of {total} designer documentation PDFs...\n")

    start_time = time.time()
    success_count = 0

    for idx, (folder, pdf_name, generator_fn) in enumerate(DOCUMENTS, start=1):
        target_folder = os.path.join(DOCS_DIR, folder)
        os.makedirs(target_folder, exist_ok=True)

        target_pdf = os.path.join(target_folder, pdf_name)
        safe_name = pdf_name.replace(".pdf", "").replace(" ", "_").replace(",", "").replace("&", "and")
        target_html = os.path.join(HTML_DIR, f"{safe_name}.html")

        # 1. Generate HTML
        html_content = generator_fn()
        with open(target_html, "w", encoding="utf-8") as f:
            f.write(html_content)

        # 2. Render to PDF via Edge
        cmd = [
            EDGE_PATH,
            "--headless",
            "--disable-gpu",
            "--run-all-compositor-stages-before-draw",
            f"--print-to-pdf={target_pdf}",
            "--no-pdf-header-footer",
            f"file:///{target_html.replace(os.sep, '/')}",
        ]

        res = subprocess.run(cmd, capture_output=True)

        if os.path.exists(target_pdf) and os.path.getsize(target_pdf) > 0:
            size_kb = round(os.path.getsize(target_pdf) / 1024, 1)
            print(f"[{idx:02d}/{total:02d}] \u2714 Rendered: {folder} / {pdf_name} ({size_kb} KB)")
            success_count += 1
        else:
            print(f"[{idx:02d}/{total:02d}] \u2716 FAILED: {folder} / {pdf_name}")
            if res.stderr:
                print("   Error:", res.stderr.decode("utf-8", errors="ignore"))

    elapsed = round(time.time() - start_time, 1)
    print(f"\n=======================================================")
    print(f"PDF Compilation Complete: {success_count}/{total} files generated in {elapsed}s")
    print(f"Target Directory: {DOCS_DIR}")
    print(f"=======================================================\n")

if __name__ == "__main__":
    build_all_pdfs()
