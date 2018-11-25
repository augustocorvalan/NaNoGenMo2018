
alt_config = {
    "output_sink": latex_sink,
    "chapter_list_to_string": latex_new_page_formatter,
    "default_paragraph_formatter": latex_unordered_list_formatter,
    "default_section_formatter": star_separator_formatter,
    "chapter_configs": [
        {"config": MorningConfig, "model": model_1_01},
        {"config": MorningConfig, "model": model_1_02},
        {"config": Config},
        {"config": MorningConfig, "model": model_2_01},
        {"config": Config},
        {"config": MorningConfig, "model": model_2_02},
        {"config": MorningConfig, "model": model_3_01},
        {"config": Config, "model": model_3_01},
        {"config": MorningConfig, "model": model_3_02},
        {"config": Config, "model": model_3_02},
    ]
}
latex_book_output_config = {
    "output_sink": latex_sink,
    "chapter_list_to_string": latex_new_page_formatter,
    "default_paragraph_formatter": latex_unordered_list_formatter,
    "default_section_formatter": star_separator_formatter,
    "chapter_configs": [
        {"config": MorningConfig, "model": model_1_01},
        {"config": MorningConfig, "model": model_1_01},
        {"config": MorningConfig, "model": model_1_01},
        # TODO morning + night
        {"config": MorningNightConfig, "model": model_1_03},
        {"config": MorningNightConfig, "model": model_1_03},
        {"config": MorningNightConfig, "model": model_1_01},
        {"config": MorningNightConfig, "model": model_1_01},
        # TODO morning + discover surveillance + night
        {"config": Config, "model": model_1_04},
        {"config": Config, "model": model_1_05},
        # TODO morning + afternoon + night
        # TODO morning + afternoon + night
        # TODO morning + afternoon + discover surveillance + night
